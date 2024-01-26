import time

from common import stage, image, color
from modules.baas import home

shop_position = {
    'cn': {'general': (150, 150), 'arena': (150, 453)},
    'jp': {'general': (150, 150), 'arena': (150, 533)},
    'intl': {'general': (150, 150), 'arena': (150, 533)},
}

goods_position = {
    1: (650, 200), 2: (805, 200), 3: (960, 200), 4: (1110, 200),
    5: (650, 460), 6: (805, 460), 7: (960, 460), 8: (1110, 460),
    9: (650, 200), 10: (805, 200), 11: (960, 200), 12: (1110, 200),
    13: (650, 460), 14: (805, 460), 15: (960, 460), 16: (1110, 460),
    17: (650, 460), 18: (805, 460), 19: (960, 460), 20: (1110, 460)
}


def to_shop(self):
    pos = {
        'home_student': (793, 645),  # 首页->商店
    }
    home.to_menu(self, 'shop_menu', pos)


def to_goods_tab(self, shop):
    cl = shop_position[self.game_server][shop]
    color.wait_rgb_similar(self, (cl[0] - 135, cl[1]), (45, 70, 99), cl=cl)


def start(self):
    # 回到首页
    home.go_home(self)
    # 到商店页面
    to_shop(self)
    # 购买商品
    buy_goods(self)
    # 回到首页
    home.go_home(self)


def buy_goods(self):
    """
    刷新并购买商品
    """
    shops = ['general', 'arena']
    for shop in shops:
        if not self.tc[shop]['enable']:
            self.logger.error(f"当前商店{shop}设置为: 不启用")
            continue
        to_goods_tab(self, shop)
        # 选择商品
        start_buy(self, shop)
        while refresh_shop(self, shop):
            start_buy(self, shop)


def start_buy(self, shop):
    """
    开始购买商品
    """
    choose_goods(self, self.tc[shop]['goods'], shop)
    if not image.compare_image(self, 'shop_choose-buy', 1):
        self.logger.error("没有选中道具")
        return

    # 检查是否可以购买
    if not color.check_rgb(self, (1200, 682), (251, 231, 68)):
        self.logger.error("货币不足，无法购买")
        return

    pos = {
        'shop_choose-buy': (1166, 661),  # 点击选择购买
    }
    ends = (
        'shop_buy-confirm1',
        'shop_buy-confirm2',
    )
    image.detect(self, ends, pos)
    # 确认购买
    self.click(700, 500, False)
    # 关闭获得奖励
    stage.close_prize_info(self, True)


def choose_goods(self, goods, shop):
    time.sleep(0.5)
    goods = sorted(goods)
    self.logger.warning("开始点击所需商品")
    swipe1 = False
    swipe2 = False
    for g in goods:
        # 一阶段滑动
        if 9 <= g <= 16 and not swipe1:
            swipe1 = True
            stage.screen_swipe(self, reset=False, f=(933, 605, 933, 50, 0.6))
        # 二阶段滑动
        elif g >= 17 and not swipe2:
            swipe2 = True
            stage.screen_swipe(self, reset=False, f=(933, 605, 933, 0, 0.1))
        # 点击商品,防止太快点不到
        time.sleep(0.2)
        self.click(*goods_position[g], False)


def refresh_shop(self, shop):
    """
    刷新商店
    """
    need_count = self.tc[shop]['count']
    purchased_count = 4 - calc_surplus_count(self)
    self.logger.warning("{0}商店 需要购买次数:{1}次 当前已购买次数{2}次".format(shop, need_count, purchased_count))
    # 次数已满
    if need_count <= purchased_count:
        # 关闭购买弹窗
        home.click_house_under(self)
        return False
    # 点击购买
    self.click(765, 460, False)
    return True


def calc_surplus_count(self):
    """
    计算剩余购买次数,这里必须用图片匹配才能精准,用文字识别小数字必出bug
    """
    self.click(1168, 660, False)
    # 等待确认购买加载
    if not image.compare_image(self, 'shop_refresh-confirm', 5):
        # 未能加载还剩0次
        return 0
    for i in range(3, 0, -1):
        if image.compare_image(self, 'shop_buy{0}'.format(i), 0, 0.9):
            return i
    return 0
