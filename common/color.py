import math
import time

import numpy as np

from common import image


def color_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)


def wait_rgb_similar(self, area, rgb, retry=999, threshold=100, rate=0.1, cl=None):
    """
    等待相似颜色出现
    """
    compare = check_rgb(self, area, rgb, threshold)
    if not compare and retry > 0:
        if cl is not None:
            self.click(*cl, False)
        time.sleep(rate)
        return wait_rgb_similar(self, area, rgb, retry - 1, threshold, rate, cl)
    return compare


def check_rgb(self, area, target_rgb=(250, 231, 69), threshold=100, ss_data=None, no_logger=False):
    """
    判断颜色是否相近，用来判断按钮是否可以点击
    """
    if ss_data is None:
        sa = np.array(self.d.screenshot())
        # 直接用 RGB 格式的色彩值
        sa_rgb = sa[area[1]][area[0]]
        get_rgb = (sa_rgb[0], sa_rgb[1], sa_rgb[2])
    else:
        bgr = ss_data[area[1]][area[0]]
        get_rgb = (bgr[2], bgr[1], bgr[0])
    dist = color_distance(target_rgb, get_rgb)
    result = dist <= threshold
    if not no_logger:
        self.logger.info("check_rgb area:%s target_rgb:%s get_rgb:%s color_dist:%.2F result:%s", area, target_rgb,
                         get_rgb,
                         dist, result)
    return result


def check_rgb_similar(self, area=(1090, 683, 1091, 684), rgb2=(75, 238, 249), threshold=20):
    """
    判断颜色是否相近，用来判断按钮是否可以点击
    """
    self.latest_img_array = self.get_screenshot_array()
    img = image.screenshot_cut(self, area, need_loading=False, ss=self.latest_img_array)
    rgb1 = img[0][0][0], img[0][0][1], img[0][0][2]
    dist = color_distance(rgb1=rgb1, rgb2=rgb2)
    result = dist <= threshold
    self.logger.info("check_rgb_similar area:%s target_rgb:%s get_rgb:%s color_dist: %s result:%s", area, rgb2, rgb1,
                     dist, result)
    return result
