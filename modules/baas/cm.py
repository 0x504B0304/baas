from common import image

x = {
    'notice': (610, 146, 640, 175),
    'skip-menu': (1177, 27, 1228, 51),
    'confirm': (737, 505, 797, 535)
}


def close_notice(self):
    """
    关闭通知
    @param self:
    """
    if image.compare_image(self, 'cm_notice', 3):
        self.click(888, 160, False)
