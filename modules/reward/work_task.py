from common import stage, color
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36),
    'receive': (1094, 657, 1206, 681),
    'reward': (369, 134, 605, 182),  # 领取奖励弹窗
}

check_btn = [{'x': (1075, 680), 'cl': (1140, 641)}, {'x': (945, 680), 'cl': (968, 666)}]


def to_work_task(self):
    pos = {
        'home_student': (62, 236),  # 首页->工作任务
    }
    home.to_menu(self, 'work_task_menu', pos)


def start(self):
    # 回到首页
    home.go_home(self)
    # 导工作任务页面
    to_work_task(self)
    for btn in check_btn:
        while True:
            if color.check_rgb(self, btn['x'], (250, 236, 74)):
                # 领取奖励
                self.click(*btn['cl'], False)
                # 关闭获得奖励
                stage.close_prize_info(self, True)
                # 点击空白处防止体力超出
                self.click(1236, 79)
            else:
                self.logger.warning("没有奖励可以领取")
                break
    # 回到首页
    home.go_home(self)
