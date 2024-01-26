from modules.baas import home


def start(self):
    # 回到首页
    home.go_home(self)
    to_group(self)
    home.go_home(self)


def to_group(self):
    pos = {
        'home_student': (535, 640),  # 首页->小组引导
        'group_guide': (310, 377),  # 小组引导-小组
        'group_sign-up-confirm': (644, 491),  # 签到奖励
    }
    home.to_menu(self, 'group_menu', pos)
