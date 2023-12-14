import os
import sys

import cv2
import numpy as np

from modules.activity import tutor_dept, summer_vacation
from modules.baas import home, restart, cm
# 图片资源数据 image assets data
from modules.daily import arena, cafe, wanted, special_entrust, shop, schedule, make, group, buy_ap
from modules.reward import mailbox, momo_talk, work_task
from modules.scan import hard_task, normal_task, main_story

iad = {
}
# 图片坐标数据 image box data
ibd = {
    'cm': cm.x,
    'home': home.x,
    'restart': restart.x,
    'arena': arena.x,
    'cafe': cafe.x,
    'group': group.x,
    'make': make.x,
    'schedule': schedule.x,
    'shop': shop.x,
    'special_entrust': special_entrust.x,
    'wanted': wanted.x,
    'mailbox': mailbox.x,
    'momo_talk': momo_talk.x,
    'work_task': work_task.x,
    'hard_task': hard_task.x,
    'normal_task': normal_task.x,
    'tutor_dept': tutor_dept.x,
    'buy_ap': buy_ap.x,
    'main_story': main_story.x,
    'summer_vacation': summer_vacation.x,
}


def init_assets_data(self, filepath='assets/images'):
    """
    初始化资源文件数据
    """
    # 默认假设我们在源代码目录下运行
    self.log_title("开始初始化资源文件")
    base_path = ''
    # 如果我们是在 PyInstaller 打包后的版本中运行，那么改变 base_path 到正确的目录
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    if hasattr(self, 'filepath'):
        filepath = self.filepath
    assets_dir = os.path.join(base_path, filepath)
    for dp, dns, fns in os.walk(assets_dir):
        for fn in fns:
            if not fn.endswith('.png'):
                continue
            filepath = os.path.join(dp, fn)
            key = os.path.relpath(filepath, assets_dir)  # 获取文件在assets目录下的相对路径作为键
            key = os.path.splitext(key)[0].replace(os.sep, '_')  # 去除文件扩展名
            iad[key] = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), -1)
    self.logger.info("资源文件初始化完成 assets:{0}".format(len(iad)))
