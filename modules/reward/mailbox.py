from common import stage, color, image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击信箱
    self.double_click(1144, 37)
    # 等待信箱页面加载
    image.compare_image(self, 'mailbox_menu')

    if color.check_rgb_similar(self):
        self.logger.info("开始领取奖励")
        # 点击一键领取
        self.click(1136, 669)
        # 关闭获得奖励
        stage.close_prize_info(self, False, True)
    else:
        self.logger.info("没有需要领取的奖励")
    # 回到首页
    home.go_home(self)
