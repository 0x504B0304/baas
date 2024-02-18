import webbrowser
from common import config
from web import configs

version = 'v2.3.0'


def open_baas():
    configs.check_config()
    ac = config.get_app_config()
    webbrowser.open_new('http://localhost:{0}?v={1}'.format(ac['port'], version))


def open_github():
    webbrowser.open_new('https://github.com/baas-pro/baas')


def open_bilibili():
    webbrowser.open_new('https://www.bilibili.com/video/BV1Dx4y1Z7nW')
