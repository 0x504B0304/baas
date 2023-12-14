import time

from common import image, stage
from common.color import detect_rgb_one_time
from modules.baas import restart

x = {
    'student': (328, 654, 346, 663),
    'cafe': (88, 651, 96, 657),  # 咖啡厅
    'cafe-black': (88, 651, 96, 657),  # 咖啡厅(用来判断无法截图)
    'menu': (611, 248, 670, 278),  # 右上角点击菜单
    'bus': (107, 9, 162, 36),  # 业务区
    'home-feature': (1203, 24, 1240, 60),  # 右上角菜单(作为主页标志)
    'quick-home': (1215, 5, 1255, 42),  # 快速回到首页,左上
    'login-feature': (1105, 601, 1142, 640),  # 登录界面
    'news': (250, 85, 328, 117),  # 公告
}


def is_home(self):
    """
    是否为首页
    """
    return image.compare_image(self, 'home_student', 0)


def go_home(self):
    """
    回到首页
    """
    self.logger.info("go home")
    app = self.d.app_current()
    if app['package'] != self.bc['baas']['base']['package']:
        # 启动游戏
        return restart.start(self)
    # 返回首页
    if recursion_click_house(self):
        return
    # 返回首页失败启动游戏
    restart.start(self)


def click_house_under(self):
    self.double_click(1236, 67, False)


def quick_method_to_main_page(self):
    """
    出现什么图标点击对应图标,直到返回首页
    """
    possibles = {
        'home_quick-home': (1236, 31),
        'normal_task_task-finish': (1038, 662),
        'normal_task_prize-confirm': (776, 655),
        'main_story_fight-confirm': (1168, 659),
        'normal_task_fail-confirm': (643, 658),
        'normal_task_fight-task-info': (420, 592),
        'normal_task_mission-operating-task-info': (1000, 664),
        'normal_task_mission-operating-task-info-notice': (416, 595),
        'normal_task_mission-pause': (768, 501),
        'normal_task_task-begin-without-further-editing-notice': (888, 163),
        'normal_task_task-operating-round-over-notice': (888, 163),
        'buy_ap_notice': (920, 167),
        'home_login-feature': (640, 360),
        'home_news': (1142, 104),
        'momo_talk_peach1': (1123, 122),
        'cafe_students-arrived': (922, 189),
        'group_sign-up-reward': (920, 159),
        'cafe_cafe-reward-status': (905, 159),
        'cafe_invitation-ticket': (835, 97),
        'summer_vacation_game_success': (1138, 666),
    }
    fail_cnt = 0
    while True:
        stage.wait_loading(self)
        self.latest_img_array = self.get_screenshot_array()  # 每次公用一张截图
        res = detect_rgb_one_time(self, [], [], ['main_page'])
        if res == ('end', 'main_page'):
            break
        click_pos = [
            [640, 100],
            [1236, 31]
        ]
        los = [
            "reward_acquired",
            "home"
        ]
        res = detect_rgb_one_time(self, click_pos, los, [])
        if res == ('click', True):
            continue

        # region 资源图片可能会出现的位置
        for asset, obj in possibles.items():
            if image.compare_image(self, asset, 0, obj[2], nl=False, ss=self.latest_img_array):
                self.logger.info("find " + asset)
                self.click(obj[0], obj[1], False)
                time.sleep(self.bc['baas']['base']['ss_rate'])
                fail_cnt = 0
                break
        else:
            fail_cnt += 1
            if fail_cnt > 10:
                fail_cnt = 0
                self.logger.info("tentative clicks")
                self.double_click(1233, 11, False)
                time.sleep(self.bc['baas']['base']['ss_rate'])
    self.double_click(851, 262, False)  # 和妹子互动
    return True


def recursion_click_house(self, check_text=False, fail_count=0):
    """
    递归点击首页按钮，如果返回False则返回首页失败，反之返回首页成功
    """
    # 多次返回失败
    if fail_count >= 100:
        self.logger.info("多次返回首页失败! 开始重启")
        return False
    if is_home(self):
        # 在首页先点击右上角
        self.click(1233, 11, False)
        # 和妹子互动
        self.double_click(851, 262, False)
        return True
    # 返回首页
    self.double_click(1233, 11, False)
    # 重新检查
    time.sleep(self.bc['baas']['base']['ss_rate'])
    if fail_count >= 10 and fail_count % 10 == 0:
        self.logger.warning('当前图片识别模式:{0} 如果一直卡识别可以打开Baas设置更换识别模式'.format(self.bc['baas']['base']['compare_mode']))
    return recursion_click_house(self, check_text, fail_count + 1)
