import time

from common import ocr, color, stage, image
from modules.baas import home
from modules.scan import hard_task

x = {
    'menu': (107, 9, 162, 36),
    'task-info': (578, 124, 702, 153),  # 任务信息弹窗
    'fight-task': (107, 9, 162, 36),  # 战斗任务弹窗
    'force-edit': (107, 9, 162, 36),  # 部队编辑界面
    'fight-skip': (1111, 531, 1136, 556),  # 跳过战斗
    'auto-over': (1072, 589, 1094, 611),  # 回合自动结束
    'force-1': (118, 548, 130, 564),
    'force-2': (118, 548, 130, 564),
    'force-3': (118, 548, 130, 564),
    'force-4': (118, 548, 130, 564),
    'box': (202, 531, 241, 570),  # 钻石宝箱
    'get-box': (614, 500, 666, 525),  # 获取宝箱
    'task-scan': (916, 218, 957, 237),  # 是否可以扫荡
    'side-quest': (360, 215, 401, 234),  # 支线任务
    'attack': (1126, 642, 1191, 670),  # 编队界面右下角出击
    'prize-confirm': (742, 642, 803, 668),  # 获得奖励确认按钮(支线通关)
    'task-finish': (1000, 648, 1063, 678),  # 任务完成确认按钮(主线通关)
    'no-pass': (198, 354, 220, 376),  # 未通关
    'move-force-confirm': (732, 483, 800, 516),  # 移动部队确认按钮
    'end-turn': (732, 483, 800, 516),  # 结束回合确认按钮
    'fight-task-info': (580, 83, 638, 113),  # 战斗过程中的任务信息弹窗
    'fail-confirm': (643, 637, 671, 676),  # 战斗失败确认按钮
    'mission-operating-task-info': (1000, 671, 1019, 679),  # 任务执行过程中任务信息(左下蓝色)
    'mission-operating-task-info-notice': (579, 81, 702, 116),  # 任务执行过程中任务信息(弹窗)
    'mission-pause': (583, 139, 707, 177),  # 中断任务
    'task-begin-without-further-editing-notice': (695, 334, 758, 365),  # 任务开始前不再编辑部队的提示
    'task-operating-round-over-notice': (598, 332, 708, 365),  # 任务执行过程中回合结束的提示
    'task-operating-feature': (13, 7, 67, 40),  # 任务执行过程中的特征（左上）
    'edit-force': (107, 9, 162, 36),  # 部队编辑
    'sss': (204, 362, 212, 434)  # 三颗星⭐️⭐️⭐️

}
normal_position = {
    1: (1120, 240), 2: (1120, 340), 3: (1120, 440), 4: (1120, 540), 5: (1120, 568),
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus', mis_fu=self.click, mis_argv=(1195, 576))

    # 点击任务
    self.click(816, 285)

    # 选择地点加载
    image.compare_image(self, 'normal_task_menu', 20, 3, False, home.click_house_under, (self,))

    if self.tc['task'] == 'hard_task':
        # 点击困难
        while not color.check_rgb_similar(self, (1000, 150, 1001, 151), (66, 66, 198)):
            self.click(1062, 154)
    else:
        # 点击普通
        while not color.check_rgb_similar(self, (700, 150, 701, 151), (88, 66, 46)):
            self.click(803, 156)
    # 开始扫荡
    start_scan(self)

    # 回到首页
    home.go_home(self)


def start_scan(self):
    prev_region = None
    swipe = False
    for tk in self.tc['config']:
        # 选择区域
        choose_region(self, tk['region'])
        if self.tc['task'] == 'hard_task':
            # 点击入场
            self.click(*hard_task.hard_position[tk['stage']])
        else:
            if prev_region == tk['region'] and swipe:
                self.swipe(933, 230, 933, 586)
                time.sleep(0.5)
            if tk['stage'] > 4:
                self.swipe(933, 586, 933, 230)
                time.sleep(0.5)
            prev_region = tk['region']
            swipe = tk['stage'] > 4
            # 点击入场
            self.click(*normal_position[tk['stage']])
        # 确认扫荡
        rst = stage.confirm_scan(self, tk['count'], 99)
        if rst == 'return':
            return
        # 关闭任务信息
        self.double_click(1236, 98)


def choose_region(self, region):
    cu_region = int(ocr.screenshot_get_text(self, (122, 178, 163, 208), self.ocrNum))
    if cu_region == region:
        return
    if cu_region > region:
        self.click(40, 360, False, cu_region - region, 0.1)
    else:
        self.click(1245, 360, False, region - cu_region, 0.1)
    return choose_region(self, region)
