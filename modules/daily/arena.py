import time

from common import ocr, color, stage, image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36),
    'edit-force': (107, 9, 162, 36),
    'id': (476, 424, 496, 442),
    'cd': (153, 516, 212, 535),
    '0-5': (194, 479, 206, 497),
    'skip': (1109, 591, 1135, 614),
    'attack': (1140, 654, 1197, 681)
}
finish_seconds = 55


def to_arena(self):
    possible = {
        'home_student': (1195, 576),
        'home_bus': (1093, 524),
    }
    image.detect(self, 'arena_menu', possible, pre_argv=home.go_home(self))


def start(self):
    # 回到首页
    home.go_home(self)

    to_arena(self)

    # 开始战斗
    start_fight(self)

    # 回到首页
    home.go_home(self)


def get_prize(self):
    if color.check_rgb_similar(self, (320, 400, 321, 401)):
        # 领取时间奖励
        self.click(353, 385)
        # 关闭奖励
        stage.close_prize_info(self)
    if color.check_rgb_similar(self, (330, 480, 331, 481)):
        # 领取挑战奖励
        self.click(348, 465)
        # 关闭奖励
        stage.close_prize_info(self)


def start_fight(self, wait=False):
    # 检查余票
    time.sleep(0.5)
    if image.compare_image(self, 'arena_0-5', 0):
        self.logger.info("没票了")
        get_prize(self)
        return True
    # 检测已有冷却
    if wait or not image.compare_image(self, 'arena_cd', 0):
        self.finish_seconds = finish_seconds
        return False
    # 选择对手
    choose_enemy(self)
    # 编队
    self.click(640, 570, True, 1, 0.5)
    # 等待出击加载
    image.compare_image(self, 'arena_edit-force', 999, 20, False, self.click, (1125, 599, False), 0.5)

    # 检查跳过是否勾选
    image.compare_image(self, 'arena_skip', 999, 20, False, self.click, (1125, 599, False), 0.5)

    # 出击
    image.compare_image(self, 'arena_edit-force', threshold=10, mis_fu=self.click, mis_argv=(1163, 658), rate=1, n=True)
    while True:
        # 检查有没有出现ID
        if image.compare_image(self, 'arena_id', 0):
            break
        # 关闭弹窗
        self.click(1235, 82, False)
        time.sleep(self.bc['baas']['base']['ss_rate'])
    start_fight(self, True)


def choose_enemy(self):
    less_level = int(self.tc['config']['less_level'])
    # 识别自己等级
    my_lv = float(ocr.screenshot_get_text(self, (165, 215, 208, 250), self.ocrNum))
    refresh = 0
    while True:
        # 超出最大次数,敌人预期等级-1
        if refresh > self.tc['config']['max_refresh']:
            less_level -= 1
            refresh = 0
            continue
        # 识别对手等级
        enemy_lv = float(ocr.screenshot_get_text(self, (551, 298, 581, 317), self.ocrNum))
        self.logger.info("对手等级 {0}".format(enemy_lv))
        if enemy_lv + less_level <= my_lv:
            break
        # 更换对手
        self.double_click(1158, 145)
        refresh += 1
    # 选择对手
    self.click(769, 251)
