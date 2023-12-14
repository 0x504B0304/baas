import time

from common import image

x = {
    'menu': (38, 628, 75, 646),
    'maintain': (604, 301, 654, 327),
    'update': (581, 147, 700, 175)
}


def only_start(self):
    # 重启应用
    pkg = self.bc['baas']['base']['package']
    self.log_title("开始打开BA")
    self.d.app_stop(pkg)
    self.d.app_start(pkg)
    # 强制等待
    time.sleep(8)


def start(self):
    only_start(self)
    pos = {
        'restart_menu': (624, 373),  # 首页菜单
        'restart_maintain': (640, 500),  # 维护
        'restart_update': (769, 501),  # 更新
        'home_news': (1142, 104),  # 公告
    }
    image.detect(self, 'home_student', pos, cl=(1233, 11))
