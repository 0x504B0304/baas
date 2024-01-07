from common import stage, image
from modules.baas import home

meet_position = {
    'cnd': (1000, 200),
    'ghn': (1000, 300),
    'qxn': (1000, 400)
}
lv_position = {
    1: (1116, 185), 2: (1116, 285), 3: (1116, 385), 4: (1116, 485),
}


def to_exchange_meeting(self):
    pos = {
        'home_student': (1200, 573),  # 首页->业务区
        'home_bus': (715, 595),  # 业务区->学园交流会
        'normal_task_task-info-window': (60, 40),  # 任务信息->关闭
        'exchange_meeting_stage-list': (60, 40)  # 关卡列表->返回
    }
    home.to_menu(self, 'exchange_meeting_menu', pos)


def start(self):
    if self.game_server == 'cn':
        return
    # 回到首页
    home.go_home(self)
    # 选择委托
    choose_meet(self)
    # 回到首页
    home.go_home(self)


def choose_meet(self):
    fns = ['cnd', 'ghn', 'qxn']
    for fn in fns:
        tk = self.tc[fn]
        if not tk['enable']:
            continue
        # 等待加载
        to_exchange_meeting(self)
        # 点击委托 等待加载 关卡列表
        image.compare_image(self, 'wanted_stage-list', cl=meet_position[fn], rate=1)
        # 点击关卡 确认扫荡
        rst = stage.confirm_scan(self, tk['stage'], tk['count'], 99, cl=lv_position[tk['stage']])
        if rst == 'return':
            break
