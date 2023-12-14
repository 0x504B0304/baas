from common import image
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36),
    'sign-up-reward': (610, 141, 673, 176)
}


def start(self):
    # 回到首页
    home.go_home(self)
    possible = {
        'home_student': (578, 648),
    }
    end = (
        'group_sign-up-reward',
        'group_menu',
    )
    res = image.detect(self, end, possible)
    if res == 'group_sign-up-reward':
        self.logger.info('get 10 AP')

    home.go_home(self)
