import time

import cv2
import numpy as np

from common import stage, image
from modules.baas import home
from modules.story import momo_talk

part_position = {
    1: (300, 250),
    2: (530, 450),
    3: (880, 250),
    4: (270, 450),
    5: (650, 250),
    'final': (850, 633)
}
chapter_position = {
    1: (1020, 315),
    2: (1020, 380),
    3: (1020, 450),
    4: (1020, 450),
    5: (1020, 505),
}


def to_main_story(self):
    pos = {
        'home_student': (1200, 573),  # 首页->业务区
        'home_bus': (1033, 260),  # 业务区->故事
        'main_story_story': (240, 350),  # 故事->主线故事
        'main_story_go-main-story': (58, 108),  # 最终装->主线剧情
        'main_story_choose-plot': (56, 38)  # 选择章节->返回
    }
    ends = ('main_story_menu1', 'main_story_menu2')
    home.to_menu(self, ends, pos)


def to_choose_story(self):
    pos = {
        'fight_fail': (647, 655)
    }
    image.detect(self, 'main_story_choose-plot', pos)


def start(self):
    # 回到首页
    home.go_home(self)
    # 开始故事
    start_story(self)
    # 回到首页
    home.go_home(self)


def check_finish(self):
    ends = (
        'main_story_clearance',  # 检查是否通关
        'main_story_current-clearance'  # 检查是否通关
    )
    return image.detect(self, ends, retry=3)


def start_admission(self):
    if check_finish(self) is not None:
        self.logger.error("剧情已经完成了")
        return
    # 查看第一个是否锁住了
    cl = (1114, 237)
    time.sleep(2)
    if image.compare_image(self, 'main_story_first-lock', 0, 0.6):
        # 锁住了点第二个任务x
        cl = (1114, 339)
    # 等待剧情信息加载
    image.detect(self, 'main_story_plot-info', cl=cl, rate=2)

    is_fight = image.compare_image(self, 'main_story_plot-fight', 0, 0.6)

    # 跳过剧情
    momo_talk.skip_plot(self)

    if is_fight:
        # 等待部队出击加载
        image.detect(self, 'fight_force-attack')
        # 点击出击,直到没有部队出击
        image.compare_image(self, 'fight_force-attack', mis_fu=self.click, mis_argv=(1163, 658), rate=1, n=True)
        if self.game_server == 'cn':
            auto_fight(self)
            time.sleep(30)
        else:
            time.sleep(3)
            stage.wait_loading(self)
            time.sleep(20)
            self.click(1235, 97)
            time.sleep(1)
            self.click(772, 500)
        # 跳过剧情
        end = skip_main_story_plot(self)
        # 作战失败
        if end == 'fight_fail':
            to_choose_story(self)
            return start_admission(self)
    else:
        # 关闭获得奖励
        stage.close_prize_info(self)
    time.sleep(3)
    # 再次递归
    return start_admission(self)


def skip_main_story_plot(self):
    pos = {
        'fight_pass-confirm': (1170, 666),  # 剧情通关
        'momo_talk_begin-relationship': (920, 568),
        'momo_talk_menu': (1205, 42),
        'momo_talk_skip': (1212, 116),
        'main_story_get-prize': (644, 634),  # 确认奖励
    }
    # 剧情这里有三种情况
    # 1. 打完架 -> 直接结束(要确认奖励) -> main_story_choose-plot
    # 2. 打完架 -> 进入剧情(要跳过剧情) -> momo_talk_confirm-skip
    # 3. 打完架 -> 作战失败(要重新开始) -> fight_fail
    ends = ('momo_talk_confirm-skip', 'fight_fail', 'main_story_choose-plot')
    end = image.detect(self, ends, pos)
    if end == 'fight_fail':
        return end
    elif end == 'momo_talk_confirm-skip':
        # 确认跳过
        self.click(770, 516, False)
        stage.close_prize_info(self, 15)


def change_acc_auto(self):  # 战斗时开启3倍速和auto
    img1 = cv2.cvtColor(np.array(self.d.screenshot()), cv2.COLOR_RGB2BGR)
    auto_r_ave = int(img1[677][1171][0]) // 2 + int(img1[677][1246][0]) // 2
    if 190 <= auto_r_ave <= 230:
        self.logger.info("将手动释放更改为自动释放")
        self.click(1215, 678)
    elif 0 <= auto_r_ave <= 60:
        self.logger.info("自动释放技能")
    else:
        self.logger.warning("无法识别自动按钮")
    acc_r_ave = int(img1[625][1196][0]) // 3 + int(img1[625][1215][0]) // 3 + int(img1[625][1230][0]) // 3
    if 250 <= acc_r_ave <= 260:
        self.logger.info("将加速阶段从 2 更改为 3")
        self.click(1215, 625)
    elif 0 <= acc_r_ave <= 60:
        self.logger.info("加速阶段 3")
    elif 140 <= acc_r_ave <= 180:
        self.logger.info("将加速阶段从 1 更改为 3")
        self.click(1215, 625, count=2)
    else:
        self.logger.warning("无法识别加速按钮")


def auto_fight(self):
    time.sleep(3)
    stage.wait_loading(self)
    time.sleep(20)
    change_acc_auto(self)
    self.logger.warning("检查自动释放技能完成")


def start_story(self):
    stage_list = self.tc['config']['stage']
    for task in stage_list:
        # 回到主菜单
        to_main_story(self)
        part, chapter = task.split('-')
        self.logger.warning(f"开始执行 {task} 剧情")
        # 选择章节
        select_part_and_chapter(self, part, chapter)
        # 开始故事
        start_admission(self)


def select_part_and_chapter(self, part, chapter):
    if self.game_server == 'cn':
        select_story_cn(self, int(part), int(chapter))
        return
    if part != 'final':
        stage.screen_swipe(self, reset=False, f=(50, 375, 1000, 375, 0.1))
        stage.screen_swipe(self, int(part), 3, reset=False, f=(820, 360, 50, 360, 0.1))
        # 选择篇幅
        self.click(*part_position[int(part)], False)
    else:
        self.click(*part_position[part], False)
    time.sleep(1)
    # 选择章节
    image.compare_image(self, 'main_story_choose-plot', cl=chapter_position[int(chapter)], rate=2)


def select_story_cn(self, part, chapter):
    """
    选择故事
    @param self:
    @return:
    """
    # 选择篇章
    self.double_click(36, 361, False)
    time.sleep(0.5)
    quotient = (part - 1) // 2
    self.click(1246, 335, False, quotient, 0.5)
    zb = 1 if part % 2 == 1 else 2
    cn_part_position = {1: (350, 345), 2: (950, 345)}
    image.compare_image(self, 'main_story_choose-plot', mis_fu=self.click, mis_argv=(*cn_part_position[zb], False))
    # 选择章节
    self.double_click(36, 361, False, 2)
    time.sleep(0.5)
    self.click(1246, 335, False, chapter - 1, 0.5)
