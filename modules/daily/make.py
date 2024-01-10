import time

from fuzzywuzzy import fuzz

from common import ocr, stage, color, image
from modules.baas import home

make_position = {
    1: (975, 279), 2: (975, 410), 3: (975, 551)
}
priority_position = {
    1: (174, 552), 2: (303, 527), 3: (414, 473), 4: (505, 388), 5: (569, 275)
}


def to_make(self):
    """
    到制造页面
    @param self:
    """
    pos = {
        'home_student': (701, 645),  # 首页->制造
    }
    home.to_menu(self, 'make_menu', pos)


def to_immediately(self):
    """
    到加速页面
    @param self:
    """
    pos = {
        'make_choose-node': (1120, 650),  # 选择节点
        'make_start-make2': (1120, 650),  # 开始制造
    }
    image.detect(self, 'make_immediately', pos, ss_rate=1)


def to_receive(self):
    """
    使用加速券到领取页面
    @param self:
    """
    pos = {
        'make_immediately': (1128, 278),  # 立即完成(加速)
        'make_confirm-acc': (771, 478)  # 确认完成(加速)
    }
    image.detect(self, 'make_receive', pos)


def to_workshop(self):
    pos = {
        'make_first-stage-start': (1120, 650)
    }
    image.detect(self, 'make_workshop', pos)


def start(self):
    if self.game_server != 'cn':
        return self.logger.critical('外服此功能待开发...')
    # 回到首页
    home.go_home(self)
    # 去制造页面
    to_make(self)
    # 清空已有制造
    if empty_make(self):
        # 开始制造
        start_make(self)
    # 回到首页
    home.go_home(self)


def empty_make(self):
    """
    清空制造
    @param self:
    @return:
    """
    ends = (
        'make_receive',
        'make_immediately',
        'make_start-make'
    )
    end = image.detect(self, ends, None)
    if end == 'make_receive':
        receive_prize(self)
    elif end == 'make_immediately':
        return make_immediately(self)
    return True


def receive_prize(self):
    """
    领取奖励
    @param self:
    """
    # 点击领取
    image.compare_image(self, 'make_receive', cl=(1122, 275), rate=1, n=True)
    # 关闭奖励
    stage.close_prize_info(self)


def make_immediately(self):
    """
    立即加速
    @param self:
    @return:
    """
    if not self.tc['config']['use_acc_ticket']:
        self.logger.error("当前配置为：不使用加速券...")
        return False
    to_receive(self)
    receive_prize(self)


def start_make(self):
    for i in range(self.tc['config']['count']):
        # 点击制造 -> 全部查看
        image.detect(self, 'make_view-all', cl=(975, 264))
        # 选择石头
        if not choose_tone(self):
            break
        # 第一阶段启动 -> 等待制造页面加载
        to_workshop(self)

        # 选择物品
        choose_item(self)
        # 到达加速页面
        to_immediately(self)
        # 立即加速
        make_immediately(self)


def choose_item(self):
    """
    根据优先级选择制造物品
    @param self:
    @return:
    """
    time.sleep(3)
    self.click(445, 552, False)
    # 选择优先级最高物品
    check_index = get_high_priority(self)
    # 选择最高优先级物品
    self.click(*priority_position[check_index + 1])
    return check_index


def get_high_priority(self):
    """
    计算优先级最高的物品
    @param self:
    @return: 优先级最高索引
    """
    # 遍历查看所有物品
    items = []
    for i, position in priority_position.items():
        self.click(*position, False)
        item = ocr.screenshot_get_text(self, (720, 204, 1134, 269))
        items.append(item)
    # 计算优先级最高的物品
    check_item = None
    check_index = 0
    for i, item in enumerate(items):
        for priority in self.tc['config']['priority']:
            ratio = fuzz.ratio(item, priority)
            if ratio < 80:
                continue
            if not check_item or \
                    self.tc['config']['priority'].index(priority) < self.tc['config']['priority'].index(check_item):
                check_item = priority
                check_index = i
    return check_index


def choose_tone(self):
    """
    选择石头
    @param self:
    @return:
    """
    # 点击拱心石
    time.sleep(1)
    self.click(908, 199, False)
    time.sleep(1)
    # 检查是否满足
    if color.check_rgb(self, (995, 631)):
        return True
    # 点击拱心石碎片
    self.click(769, 200, False, 10)
    time.sleep(1)
    return color.check_rgb(self, (995, 631))
