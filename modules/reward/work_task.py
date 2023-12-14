from common import stage, color, image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击工作任务
    self.double_click(62, 236)
    # 等待工作任务页面加载
    image.compare_image(self, 'work_task_menu')

    while True:
        if color.check_rgb_similar(self):
            self.logger.info("开始领取奖励")
            # 点击一键领取
            self.click(1136, 669)
            # 关闭获得奖励
            stage.close_prize_info(self, True)
            # 点击空白处防止体力超出
            self.click(1236, 79)
        else:
            self.logger.info("没有奖励可以领取")
            break

    # 回到首页
    home.go_home(self)
