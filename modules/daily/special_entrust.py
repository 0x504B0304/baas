import time

from common import ocr, stage, image
from modules.baas import home

x = {
}
entrust_position = {
    'jdfy': (962, 270), 'xyhs': (962, 410)
}
level_position = {
    1: (1116, 185), 2: (1116, 285), 3: (1116, 385), 4: (1116, 485), 5: (1116, 585),
    6: (1116, 330), 7: (1116, 430), 8: (1116, 530), 9: (1116, 630),
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus', mis_fu=self.click, mis_argv=(1195, 576))

    # 点击特别委托
    self.click(727, 570)
    # 选择委托
    choose_entrust(self, entrust_position)
    # 回到首页
    home.go_home(self)


def choose_entrust(self, position):
    for tk in self.tc['config']:
        # 等待加载
        wait_loading_entrust(self)
        # 选择委托
        self.click(*position[tk['entrust']])
        # 等待加载
        ocr.screenshot_check_text(self, '关卡列表', (889, 99, 979, 125))

        part1_swipe = False
        part2_swipe = False

        if tk['stage'] <= 5 and not part1_swipe:
            part1_swipe = True
            self.swipe(933, 230, 933, 586)
            time.sleep(0.5)
        if tk['stage'] >= 6 and not part2_swipe:
            part2_swipe = True
            self.swipe(933, 586, 933, 230)
            time.sleep(0.5)
        # 点击关卡
        self.click(*level_position[tk['stage']])
        # 确认扫荡
        rst = stage.confirm_scan(self, tk['count'], 9)
        if rst == 'return':
            return
        elif rst == 'continue':
            continue
        # 返回委托
        back_entrust(self)


def back_entrust(self):
    # 查看是否有任务信息弹窗
    if not ocr.screenshot_check_text(self, '任务信息', (574, 122, 709, 155), 5, 0.5):
        return
    self.click(56, 38, 0, 2, 1)


def wait_loading_entrust(self):
    # 等待加载
    if self.tc['task'] == 'special_entrust':
        ocr.screenshot_check_text(self, '信用回收', (1044, 362, 1222, 414))
    else:
        ocr.screenshot_check_text(self, '讲堂', (1126, 506, 1222, 557))
