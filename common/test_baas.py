import json
import time
import unittest

import cv2
import numpy as np
import uiautomator2 as u2
from cnocr import CnOcr
from skimage.metrics import structural_similarity
from skimage.metrics import structural_similarity as compare_ssim

from common import image, config, position, stage, log, color
from modules.baas import home
from modules.exp.normal_task import exp_normal_task
from modules.scan import normal_task


class TestBaas(unittest.TestCase):

    def load_config(self):
        filepath = config.config_filepath(self.con)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.bc = data
        pass

    def log_title(self, msg):
        self.logger.info(log.title(msg))

    def setUp(self) -> None:
        self.flag_run = True
        self.screenshot_interval = 0.3
        self.click_time = 0.0
        self.latest_img_array = None
        self.con = 'kc'
        self.load_config()
        self.logger = log.create_logger(self.con, False)
        self.d = u2.connect(self.bc['baas']['base']['serial'])
        self.ocr = CnOcr()
        self.ocrEN = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
        self.ocrNum = CnOcr(det_model_name='number-densenet_lite_136-fc', rec_model_name='number-densenet_lite_136-fc')
        self.file_path = "../assets/images"
        position.init_assets_data(self, self.file_path)
        data = json.load(open(config.get_froze_path('../assets/rgb_feature/rgb_feature.json')))
        self.rgb_feature = data["rgb_feature"]

    def click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            self.logger.info("click x:%s y:%s", x, y)
            if rate > 0:
                time.sleep(rate)
            self.d.click(x, y)

    def click_condition(self, x, y, cond, fn, fn_args, wait=True, rate=0):
        """
        条件点击，直到不满足条件为止
        @param x: x坐标
        @param y: y坐标
        @param cond: true 或 false
        @param fn: 要执行的函数，需要返回bool
        @param fn_args: 执行函数的参数
        @param wait: 是否需要等待加载
        @param rate: 每次点击等待时间
        """
        if wait:
            stage.wait_loading(self)
        self.click(x, y, False)
        while cond != fn(self, *fn_args):
            time.sleep(rate)
            self.d.click(x, y)

    def double_click(self, x, y, wait=True, count=1, rate=0):
        if wait:
            stage.wait_loading(self)
        for i in range(count):
            self.logger.info("double_click x:%s y:%s", x, y)
            if rate > 0:
                time.sleep(rate)
            self.d.double_click(x, y)

    def test_task(self):
        print(color.check_rgb_similar(self, (832, 103, 833, 104), (77, 55, 40)))
        print(color.check_rgb_similar(self, (1002, 103, 1003, 104), (77, 55, 40)))
        print(color.check_rgb_similar(self, (1082, 103, 1083, 104), (106, 71, 43)))
        # print(ocr.screenshot_get_text(self, (189, 197, 228, 225), self.ocrNum))
        # assert color.check_rgb_similar(self, (124, 429, 125, 430), (75, 233, 246))

    def ss_task_lv(self, base, lv, region):
        d = "{0}/{1}".format(self.file_path, base)
        f = "../assets/images/{0}/{1}-{2}.png".format(base, region, lv)
        image.screenshot_cut(self, (191, 199, 265, 224), 0, False, d, f)
        self.click(1167, 355)
        time.sleep(3)

    def test_gen_normal_task(self):
        base = 'normal_task'
        for region in range(6, 16):
            for lv in range(1, 6):
                self.ss_task_lv(base, lv, region)

    def test_gen_hard_task(self):
        base = 'hard_task'
        for region in range(6, 16):
            for lv in range(1, 4):
                self.ss_task_lv(base, lv, region)

    def test_image(self):
        # 读取图片
        s1_img = cv2.imread('../runtime/restart_menu.png')
        s2_img = cv2.imread('../assets/images/restart/menu.png')
        # 计算差异值
        diff = cv2.absdiff(s1_img, s2_img)
        # 计算MSE（Mean Squared Error）
        mse = np.mean(diff ** 2)
        print(f"MSE: {mse}")

        # 转换图片到灰度
        grayA = cv2.cvtColor(s1_img, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(s2_img, cv2.COLOR_BGR2GRAY)
        # 计算SSIM（Structural Similarity Index）
        ssim = structural_similarity(grayA, grayB)
        print(f"SSIM: {ssim}")

    def calculate_ssim(self, imageA, imageB):
        # 转换图片到灰度
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # 计算两个灰度图像的SSIM，并获取差异图像
        (ssim, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {} {}".format(ssim, diff))

    def get_screenshot_array(self):
        return cv2.cvtColor(np.array(self.d.screenshot()), cv2.COLOR_RGB2BGR)

    def test_exp_task(self):
        """
        测试运行关卡-开图
        """
        # task = 'exp_normal_task'
        task = 'exp_hard_task'
        levels = [
            '10-1-box',
            # '10-2', '10-3'
            # '11-1', '11-2', '11-3', '11-4', '11-5',
            # '12-1', '12-2', '12-3', '12-4', '12-5',
            # '13-1', '13-2', '13-3', '13-4', '13-5',
            # '14-1', '14-2', '14-3', '14-4', '14-5',
            # '15-1', '15-2', '15-3', '15-4', '15-5',
        ]

        # 回到首页
        home.go_home(self)
        possible = {
            'home_student': (1195, 576),
            'home_bus': (815, 285),
        }
        image.detect(self, 'normal_task_menu', possible)
        for lv in levels:
            lv_data = lv.split('-')
            region = int(lv_data[0])
            lv_index = int(lv_data[1])
            self.tc = self.bc[task]
            self.tc['task'] = task
            # 选择任务模式
            exp_normal_task.choose_mode(self)
            self.stage_data = exp_normal_task.get_stage_data(self, region)
            normal_task.choose_region(self, region)
            exp_normal_task.wait_task_info(self, True)
            self.click(1172, 358, False, lv_index - 1, 1)
            time.sleep(1)
            exp_normal_task.start_fight(self, region, lv)

    def test_ss(self):
        """
        测试资源截图生成图片资源
        """
        assets = [
            # 'summer_vacation_title',
            # 'summer_vacation_skip',
            # 'summer_vacation_guide',
            # 'summer_vacation_menu',
            # 'summer_vacation_mhd-menu',
            # 'summer_vacation_enter',
            # 'summer_vacation_fight-confirm',
            # 'summer_vacation_game-unlock',

            # 'make_menu',
            # 'make_receive',
            # 'make_start-make',
            # 'make_immediately',
            # 'make_workshop',
            # 'make_start',
            # 'make_view-all',
            # 'make_choose-node',
            # 'make_confirm-acc',

            # 'home_cafe',
            # 'home_cafe-lock',
            # 'home_bus',
            # 'home_bus1',
            # 'home_student',

            # 'restart_menu',
            # 'restart_maintain',
            # 'restart_update',

            # 'arena_id',
            # 'arena_cd',
            'arena_0-5',
            # 'arena_skip',
            # 'arena_attack',
            # 'arena_menu',
            # 'arena_edit-force',

            # 'cafe_0.0',
            # 'cafe_menu',
            # 'cafe_inc-fav',

            # 'tutor_dept_entry',
            # 'tutor_dept_title',

            # 'group_menu',

            # 'mailbox_menu',

            # 'momo_talk_no-chat',
            # 'momo_talk_sort-field',
            # 'momo_talk_sort-direction',
            # 'momo_talk_menu',
            # 'momo_talk_skip',
            # 'momo_talk_confirm-skip',

            # 'work_task_menu',

            # 'shop_menu',
            # 'shop_buy3',
            # 'shop_buy2',
            # 'shop_buy1',
            # 'shop_confirm',

            # 'schedule_menu',
            # 'normal_task_menu',
            # 'normal_task_task-info',
            # 'normal_task_fight-task',
            # 'normal_task_force-edit',
            # 'normal_task_fight-skip',
            # 'normal_task_auto-over',
            # 'normal_task_sss',
            # 'normal_task_force-4',
            # 'normal_task_force-3',
            # 'normal_task_force-2',
            # 'normal_task_force-1',
            # 'normal_task_task-scan',
            # 'normal_task_15-1',
            # 'normal_task_15-2',
            # 'normal_task_15-3',
            # 'normal_task_15-4',
            # 'normal_task_15-5',
            # 'normal_task_side-quest',
            # 'normal_task_attack',
            # 'normal_task_prize-confirm',
            # 'normal_task_no-pass',
            # 'normal_task_move-force-confirm',
            # 'normal_task_end-turn',
            # 'normal_task_task-finish',
            # 'normal_task_box',
            # 'normal_task_get-box',
            # 'normal_task_fight-task-info',

            # 'buy_ap_notice',
            # 'buy_ap_notice2',
            # 'buy_ap_limited',
            # 'buy_ap_buy20',
            # 'buy_ap_buy19',
            # 'buy_ap_buy18',
            # 'buy_ap_buy17',
            # 'buy_ap_buy16',
            # 'buy_ap_buy15',
            # 'buy_ap_buy14',
            # 'buy_ap_buy13',
            # 'buy_ap_buy12',
            # 'buy_ap_buy11',
            # 'buy_ap_buy10',
            # 'buy_ap_buy9',
            # 'buy_ap_buy8',
            # 'buy_ap_buy7',
            # 'buy_ap_buy6',
            # 'buy_ap_buy5',
            # 'buy_ap_buy4',
            # 'buy_ap_buy3',
            # 'buy_ap_buy2',
            # 'buy_ap_buy1',

            # 'main_story_menu',
            # 'main_story_story',
            # 'main_story_choose-plot',
            # 'main_story_clearance',
            # 'main_story_current-clearance',
            # 'main_story_plot-info',
            # 'main_story_skip-menu',
            # 'main_story_first-lock',
            # 'main_story_plot-fight',
            # 'main_story_plot-attack',
            # 'main_story_fight-parse',
            # 'main_story_fight-confirm',
            # 'main_story_fight-fail',
            # 'main_story_auto',
            # 'main_story_three-times',
            # 'cm_confirm'
        ]
        for asset in assets:
            base, file = asset.rsplit('_', 1)
            d = "{0}/{1}".format(self.file_path, base)
            f = "../assets/images/{0}/{1}.png".format(base, file)
            image.screenshot_cut_old(self, image.get_box(asset), 0, False, d, f)
        time.sleep(1)
        self.setUp()
        for i in range(10):
            for asset in assets:
                image.compare_image(self, asset, 0)
        assert True

    def test_crop(self):
        ss = cv2.imread('../assets/images/cafe/happy-face5.png')
        file = "../assets/images/cafe/happy-face55.png"
        area = (21, 15, 48, 42)
        # OpenCV中图像的剪裁方式：img[y1:y2, x1:x2]
        img = ss[area[1]:area[3], area[0]:area[2]]
        # 使用OpenCV保存剪裁后的图像
        cv2.imwrite(file, img)
        img.save(file)
