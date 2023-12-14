from common import image
from modules.baas import home
from modules.daily import special_entrust

x = {
}
entrust_position = {
    'gjgl': (950, 270), 'smtl': (950, 415), 'jt': (950, 550)
}


def start(self):
    # 回到首页
    home.go_home(self)
    # 点击业务区
    self.double_click(1195, 576)
    # 等待业务区页面加载
    image.compare_image(self, 'home_bus', mis_fu=self.click, mis_argv=(1195, 576))

    # 点击悬赏通缉
    self.click(733, 472)
    # 选择委托
    special_entrust.choose_entrust(self, entrust_position)
    # 回到首页
    home.go_home(self)
