import time

from common import stage, ocr, image, color
from modules.baas import home

x = {
    'menu': (1178, 28, 1226, 51),
    'skip': (1195, 109, 1226, 128),
    'confirm-skip': (737, 509, 797, 534),
    'peach1': (144, 107, 169, 130),
    'peach2': (144, 107, 169, 130),
    'peach3': (144, 107, 169, 130),
    'peach4': (144, 107, 169, 130),
    'sort-field': (493, 168, 527, 185),
    'sort-direction': (634, 169, 645, 186),
}


def start(self):
    # 回到首页
    home.go_home(self)

    # 查看可以互动的学生
    if not color.check_rgb(self, (183, 125), (232, 68, 0)):
        self.logger.info("没有可以互动的学生")
        return
    # 点击桃信
    self.double_click(170, 144)
    # 等待桃信页面加载
    ocr.screenshot_check_text(self, '成员', (226, 167, 277, 189))
    # 点击短信tab
    self.click(174, 272)
    # 等短信页面加载
    ocr.screenshot_check_text(self, '未读信息', (226, 167, 321, 189))

    # 查看排序
    check_sort(self)

    # 查看第一个学生是否可以聊天
    time.sleep(0.5)
    if not color.check_rgb(self, (657, 259), (251, 71, 25)):
        home.go_home(self)
        self.logger.info("没有可以互动的学生")
        return

    # 点击第一个学生
    self.click(471, 251)
    # 开始聊天
    start_chat(self)
    # 关闭桃信
    self.click(1121, 125)
    # 重新桃信
    start(self)


def check_sort(self):
    if not image.compare_image(self, 'momo_talk_sort-field', 0):
        self.click(509, 175, False)
        time.sleep(0.5)
        self.click(449, 293, False)
        self.click(451, 370, False)
    image.compare_image(self, 'momo_talk_sort-direction', mis_fu=self.click, mis_argv=(625, 180, False), rate=0.5)


def start_chat(self):
    self.mm_i = 0
    while self.mm_i < 3:
        # 检测回复
        ex, position = ocr.screenshot_get_position(self, '回复', (774, 196, 1123, 603), 0, 0)
        if ex:
            self.mm_i = 0
            reply_message(self, position)
            continue
        # 检测好感故事
        ex, position = ocr.screenshot_get_position(self, '好感故事', (774, 196, 1123, 603), 0, 0)
        if ex:
            self.mm_i = 0
            good_story(self, position)
            continue
        # 检查文字是否发生变动
        check_message(self)
        # 三种情况都不满足等待0.5秒
        time.sleep(0.5)


def reply_message(self, position):
    # 往回复的下方移动60px点击第一条回复
    self.click(774 + position[1][0], 196 + position[1][1] + 60)
    self.logger.info("开始回复妹子")


def good_story(self, position):
    # 往回复的下方移动60px点击第一条回复
    self.click(774 + position[1][0], 196 + position[1][1] + 60)
    # 检测好感故事
    ocr.screenshot_check_text(self, '进入好感故事', (820, 545, 1017, 579))
    # 点击进入好感故事
    self.click(919, 563)
    pos = {
        'momo_talk_menu': (1205, 42),
        'momo_talk_skip': (1212, 116)
    }
    image.detect(self, 'momo_talk_confirm-skip', pos)
    # 确认跳过
    self.click(770, 516, False)
    # 关闭奖励
    stage.close_prize_info(self, True)


def check_message(self):
    # 检查文字是否发生变动
    out = ocr.screenshot_cut_get_text(self, (774, 196, 1123, 603), 0, False)
    if len(out) == 0:
        self.mm_i += 1
        return
    latest_text = out[-1].get('text')
    if not hasattr(self, 'mm_prev') or self.mm_prev == latest_text:
        self.mm_i += 1
    self.mm_prev = latest_text
