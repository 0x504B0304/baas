import time

import cv2
import numpy as np

from common import ocr
from common.color import judge_rgb_range
from modules.baas import home


def confirm_scan(self, ct, max_count):
    # 等关卡加载
    ct = int(ct)
    ocr.screenshot_check_text(self, '任务信息', (574, 122, 709, 155))
    if ct >= max_count:
        self.double_click(1034, 299, False)
        self.double_click(1034, 299, False)
        self.d.long_click(1034, 299, 5)
    else:
        # 扫荡指定次数
        self.click(1034, 299, False, int(ct) - 1, 0.6)
    # 点击开始扫荡
    self.click(938, 403, False)
    # 判断困难次数
    if self.tc['task'] == 'hard_task':
        # 查看次数是否足够
        if ocr.screenshot_check_text(self, '是否恢复挑战次数', (522, 251, 729, 279), 0, 0.5):
            self.double_click(1236, 98, False)
            return 'continue'
    # 判断统计悬赏票数
    if self.tc['task'] == 'wanted':
        # 查看入场券是否足够
        if ocr.screenshot_check_text(self, '移动', (730, 485, 803, 516), 0, 0.5):
            # 下一个
            self.click(56, 38, 0, 3)
            return 'continue'
    else:
        # 查看体力是否足够
        if ocr.screenshot_check_text(self, '是否购买', (515, 227, 627, 260), 0, 0.5):
            # 关闭弹窗 返回首页
            home.go_home(self)
            return 'return'

    # 等待确认加载
    ocr.screenshot_check_text(self, '通知', (599, 144, 675, 178))
    # 确认扫荡
    self.click(770, 500, False)
    # 检查跳过,最多检查30次
    if ct >= 3:
        ocr.screenshot_check_text(self, '跳过', (600, 488, 684, 526), 30)
        # 点击跳过
        self.click(641, 504, False)
    # 等待结算,这里很有可能会升级点击关闭升级弹窗
    while not ocr.screenshot_check_text(self, '确认', (597, 562, 680, 600), 0):
        self.click(850, 582, False)
        time.sleep(1)
    # 确认奖励
    self.click(641, 580, False)
    return 'nothing'


def close_prize_info(self, ap_check=False, mail_check=False):
    """
    关闭奖励道具结算页面
    """
    if ocr.screenshot_check_text(self, '点击继续', (577, 614, 704, 648), 1):
        # 关闭道具信息
        self.click(640, 635)
        time.sleep(0.5)
        return
    if ap_check and ocr.screenshot_check_text(self, '因超出持有上限', (532, 282, 724, 314), 1):
        self.click(650, 501)
        return
    if mail_check and ocr.screenshot_check_text(self, '以上道具的库存已满', (508, 388, 745, 419), 1):
        self.click(642, 527)
        return
    return close_prize_info(self, ap_check, mail_check)


def wait_loading(self):
    """
    检查是否加载中，
    """
    t_start = time.time()
    while 1:
        self.latest_img_array = cv2.cvtColor(np.array(self.d.screenshot()), cv2.COLOR_RGB2BGR)
        if not judge_rgb_range(self.latest_img_array, 937, 648, 200, 255, 200, 255, 200, 255) or not \
                judge_rgb_range(self.latest_img_array, 919, 636, 200, 255, 200, 255, 200, 255):
            loading_pos = [[929, 664], [941, 660], [979, 662], [1077, 665], [1199, 665]]
            rgb_loading = [[200, 255, 200, 255, 200, 255], [200, 255, 200, 255, 200, 255],
                           [200, 255, 200, 255, 200, 255], [200, 255, 200, 255, 200, 255],
                           [255, 255, 255, 255, 255, 255]]
            t = len(loading_pos)
            for i in range(0, t):
                if not judge_rgb_range(self.latest_img_array, loading_pos[i][0], loading_pos[i][1], rgb_loading[i][0],
                                       rgb_loading[i][1], rgb_loading[i][2], rgb_loading[i][3],
                                       rgb_loading[i][4], rgb_loading[i][5]):
                    break
            else:
                t_load = time.time() - t_start
                self.logger.info("loading, t load : " + str(t_load))
                if t_load > 20:
                    self.logger.warning("LOADING TOO LONG add screenshot interval to 1")
                    self.screenshot_interval = 1
                time.sleep(self.screenshot_interval)
                continue

        return True
