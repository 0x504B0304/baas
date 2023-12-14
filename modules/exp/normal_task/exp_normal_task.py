import importlib
import time

import cv2
import numpy as np

from common import ocr, color, image
from modules.baas import home
from modules.scan import main_story

x = {
}
# 普通关卡坐标
normal_position = {
    1: (1120, 240), 2: (1120, 340), 3: (1120, 440), 4: (1120, 540), 5: (1120, 568),
}
# 部队1234坐标
force_position = {
    1: (124, 195), 2: (124, 277), 3: (124, 354), 4: (124, 429),
}


def start(self):
    # 回到首页
    home.go_home(self)
    possible = {
        'home_student': (1195, 576),
        'home_bus': (815, 285),
    }
    image.detect(self, 'normal_task_menu', possible)
    # 选择任务模式
    choose_mode(self)
    # 开始战斗
    for region in self.tc['config']['region']:
        self.stage_data = get_stage_data(self, region)
        if self.stage_data is None:
            continue
        start_fight(self, region)

    # 回到首页
    home.go_home(self)


def choose_mode(self):
    """
    选择任务模式
    @param self:
    """
    self.latest_img_array = self.get_screenshot_array()
    if self.tc['task'] == 'exp_hard_task':
        while not color.judge_rgb_range(self.latest_img_array, 961, 148, 188, 208, 56, 76, 55, 75):
            self.click(1185, 147)
            self.latest_img_array = self.get_screenshot_array()

        return
    while not color.judge_rgb_range(self.latest_img_array, 680, 138, 36, 56, 56, 76, 77, 97):
        self.click(927, 147)
        self.latest_img_array = self.get_screenshot_array()


def start_fight(self, region, gk=None):
    # 选择区域
    gk_none = gk is None
    if gk_none:
        # 选择区域
        choose_region(self, region)
        gk = calc_need_fight_stage(self, region)
        if gk is None:
            self.logger.critical("本区域没有需要开图的任务关卡...")
            return
    # 点击开始任务
    if gk == 'side':
        self.click(645, 511)
    else:
        if gk not in self.stage_data:
            self.logger.critical("本关卡{0}尚未支持开图，正在全力研发中...".format(gk))
            return
        self.click(947, 540)
    # 等待地图加载

    # 遍历start需要哪些队伍
    if gk == "side":
        # 选择支线部队开始战斗
        start_choose_side_team(self, self.tc['config'][self.stage_data[str(region)]['side']])
        time.sleep(1)
        self.click(1171, 670)
        # 自动战斗
        main_story.auto_fight(self)
    else:
        prev_index = 0
        for n, p in self.stage_data[gk]['start'].items():
            cu_index = choose_team(self, gk, n)
            if cu_index < prev_index:
                self.exit("队伍配置错误,请根据开图区域设置主队编号小于副队编号")
            prev_index = cu_index
        # 点击开始任务
        start_mission(self)

        # 检查跳过战斗
        image.compare_image(self, 'normal_task_fight-skip', threshold=10, mis_fu=self.click, mis_argv=(1123, 545),
                            rate=2)
        # 检查回合自动结束
        image.compare_image(self, 'normal_task_auto-over', threshold=10, mis_fu=self.click, mis_argv=(1082, 599),
                            rate=2)
        start_action(self, gk, self.stage_data)  # 开始战斗
        main_story.auto_fight(self)  # 自动战斗

    # 手动打boss配置
    if 'manual_boss' in self.tc['config'] and self.tc['config']['manual_boss']:
        self.click(1235, 41)

    possible = {
        'normal_task_auto-over': (1082, 599),
        'normal_task_task-finish': (1038, 662),
        'normal_task_prize-confirm': (776, 655),
        'main_story_fight-confirm': (1168, 659),
    }
    image.detect(self, 'normal_task_menu', possible)

    choose_region(self, region - 1)
    # 重新开始本区域探索
    if gk_none:
        return start_fight(self, region)


def get_stage_data(self, region):
    # 动态生成完整的模块路径
    if self.tc['task'] == 'exp_hard_task':
        module_path = f'modules.exp.hard_task.stage_data.ht_{region}'
    else:
        module_path = f'modules.exp.normal_task.stage_data.nt_{region}'
    # 导入指定的模块
    try:
        stage_module = importlib.import_module(module_path)
        stage_data = getattr(stage_module, 'stage_data', None)
        # 从该模块中获取stage_data数据
        return stage_data
    except ModuleNotFoundError:
        self.logger.critical("当前区域 {0} 尚未支持开图，正在全力研发中...".format(region))
        return None


def check_task_state(self):
    """
    检查任务当前类型
    @param self:
    @return:
    """
    # 等待任务信息弹窗加载
    wait_task_info(self)
    time.sleep(1)
    # 支线
    if image.compare_image(self, 'normal_task_side-quest', 0):
        return 'side'
    # 困难主线-可拿礼物
    if self.tc['task'] == 'exp_hard_task' and image.compare_image(self, 'normal_task_box', 0):
        return 'box'
    # 主线-三星
    if image.compare_image(self, 'normal_task_task-scan', 0):
        return 'sss'
    # 主线-未通关
    if image.compare_image(self, 'normal_task_no-pass', 0):
        return 'no-pass'
    # 主线-已通关
    return 'pass'


def wait_task_info(self, open_task=False, max_retry=99999):
    """
    等待任务信息弹窗加载
    @param self:
    @return:
    """
    while max_retry > 0:
        # 主线任务
        if image.compare_image(self, 'normal_task_task-info', 0):
            return 'main'
        # 支线任务
        if image.compare_image(self, 'normal_task_side-quest', 0):
            return 'side'
        time.sleep(0.1)
        # 是否要打开入场
        if open_task:
            self.click(1118, 239)
            time.sleep(1)
        max_retry -= 1
        self.logger.error("max_retry {0}".format(max_retry))
    return None


def calc_need_fight_stage(self, region):
    """
    查找需要战斗的关卡
    @param self:
    @param region:
    @return:
    """
    wait_task_info(self, True)
    fail = 0
    while True:
        # 等待任务信息加载
        task_state = check_task_state(self)
        self.logger.info("当前关卡状态为:{0}".format(task_state))
        # 未通关支线
        if task_state == 'side':
            self.logger.info("未通关支线，开始支线战斗")
            return task_state
        # 未通关主线
        if task_state == 'no-pass':
            self.logger.info("未通关主线，开始主线战斗")
            return get_stage(self, region, task_state)
        # 模式2 ⭐️⭐️⭐️  或者 ⭐️⭐️⭐️+宝箱礼物
        if self.tc['config']['mode'] == 2:
            if task_state == 'box':
                self.logger.info("发现星辉石宝箱，开始主线战斗")
                return get_stage(self, region, task_state)
            if task_state != 'sss':
                self.logger.info("未三星通关，开始主线战斗")
                return get_stage(self, region, task_state)
        # 点击下一关
        self.logger.warn("不满足战斗条件,查找下一关")
        self.click(1172, 358)
        # 检测是否还在本区域
        fail += 1
        if fail >= 5:
            time.sleep(1)
            if region != ocr.screenshot_get_text(self, (189, 197, 228, 225), self.ocrNum):
                return None


def get_stage(self, region, task_state):
    for i in range(1, 6):
        s = '{0}-{1}'.format(region, i)
        try:
            if image.compare_image(self, 'normal_task_' + s, 0, box=(191, 199, 265, 224)):
                if task_state == 'box':
                    return s + '-box'
                return s
        except KeyError:
            self.logger.critical("当前关卡{0}尚未支持开图，正在全力研发中...".format(s))
            return None
    return None


def get_force(self):
    """
    获取左下角部队编号
    由于ocr将1识别为7,所以7都识别为1
    """
    self.latest_img_array = cv2.cvtColor(np.array(self.d.screenshot()), cv2.COLOR_RGB2BGR)
    img = self.latest_img_array[542:570, 116:131]
    ocr_res = self.ocrNum.ocr_for_single_line(img)["text"]
    if ocr_res == "":
        return get_force(self)
    if ocr_res == "7":
        return 1
    return int(ocr_res)


def end_round(self):
    """
    结束回合
    """
    click_pos1 = [
        [1170, 670],
        [794, 207],
    ]
    lo1 = [
        "normal_task_mission_operating",
        "present",
    ]
    end1 = ["round_over_notice"]
    color.common_rgb_detect_method(self, click_pos1, lo1, end1)
    click_pos2 = [[767, 501]]
    lo2 = ["round_over_notice"]
    end2 = ["normal_task_mission_operating"]
    color.common_rgb_detect_method(self, click_pos2, lo2, end2)


def confirm_teleport(self):
    """
    确认传送并回到任务进行中界面
    """
    end1 = ["formation_teleport_notice"]
    color.common_rgb_detect_method(self, [], [], end1)
    click_pos2 = [[767, 501]]
    lo2 = ["formation_teleport_notice"]
    end2 = ["normal_task_mission_operating"]
    color.common_rgb_detect_method(self, click_pos2, lo2, end2)


def start_action(self, gk, stage_data):
    actions = stage_data[gk]['action']
    for i, act in enumerate(actions):
        # 行动前置等待时间
        if 'before' in act:
            self.logger.info("前置等待{0}秒".format(act['before']))
            time.sleep(act['before'])
        # 每次行动强制等1s
        time.sleep(1)
        msg = "开始 {0} 次行动".format(i + 1)
        if 'desc' in act:
            msg += ' desc:{0}'.format(act['desc'])
        self.logger.info(msg)
        force_index = get_force(self)
        if act['t'] == 'click':
            self.click(*act['p'])
        elif act['t'] == 'exchange':
            self.logger.info("更换部队")
            self.click(83, 557)
        elif act['t'] == 'move':
            self.logger.info("确认移动部队")
            confirm_teleport(self)
        elif act['t'] == 'end-turn':
            self.logger.info("结束回合")
            end_round(self)
        if 'ec' in act:  # 判断是否存在exchange事件
            # 等待换队
            self.logger.info("等待队伍更换事件...")
            origin = force_index
            while force_index == origin:
                force_index = get_force(self)
        # 行动后置等待时间
        if 'after' in act:
            self.logger.info("后置等待{0}秒".format(act['after']))
            time.sleep(act['after'])

        if 'wait-over' in act:
            self.logger.info("等待战斗结束...")
            wait_over(self)
            time.sleep(2)  # 就算弹出任务信息也要等待2s，否则会出现点击不到的情况
        if i != len(actions) - 1:  # 每次行动结束固定回到任务进行中界面
            to_normal_task_mission_operation_page(self)


def start_choose_side_team(self, index):
    """
    @param i: 编队编号
    到达编队页面
    """
    self.logger.info("根据当前配置,选择部队{0}".format(index))
    if index == -1:
        self.exit("你没有未配置部队,请根据开图区域设置对应属性的部队编号")
    loy = [195, 275, 354, 423]
    y = loy[index - 1]
    click_pos = [
        [74, y],
        [74, y],
        [74, y],
        [74, y],
    ]
    los = [
        "formation_edit1",
        "formation_edit2",
        "formation_edit3",
        "formation_edit4",
    ]
    ends = [
        "formation_edit" + str(index)
    ]
    los.pop(index - 1)
    click_pos.pop(index - 1)
    color.common_rgb_detect_method(self, click_pos, los, ends)


def choose_region(self, region):
    """
    选择区域
    """
    cu_region = int(ocr.screenshot_get_text(self, (122, 178, 163, 208), self.ocrNum))
    if cu_region == region:
        return
    if cu_region > region:
        self.click(40, 360, wait=False, count=cu_region - region, rate=0.1)
    else:
        self.click(1245, 360, wait=False, count=region - cu_region, rate=0.1)
    return choose_region(self, region)


def choose_team(self, gk, force):
    index = self.tc['config'][self.stage_data[gk]['attr'][force]]
    self.logger.info("根据当前配置,选择部队{0}".format(index))
    if index == -1:
        self.exit("你没有未配置部队,请根据开图区域设置对应属性的部队编号")
    to_formation_edit_i(self, index, self.stage_data[gk]['start'][force])
    if color.judge_rgb_range(self.latest_img_array, 1166, 684, 250, 255, 105, 125, 68, 88) and color.judge_rgb_range(
            self.latest_img_array, 1156, 626, 250, 255, 105, 125, 68, 88):
        self.exit("配队重复,请根据开图区域设置对应属性的部队编号")
    to_normal_task_wait_to_begin_page(self)
    return index


def to_normal_task_mission_operation_page(self):
    """
    到达任务开始后界面
    """
    click_pos = [
        [886, 162],
        [890, 162],
        [995, 102],
        [794, 207],
    ]
    los = [
        "formation_teleport_notice",
        "round_over_notice",
        "normal_task_mission_info",
        "present",
    ]
    ends = ["normal_task_mission_operating"]
    color.common_rgb_detect_method(self, click_pos, los, ends)


def to_normal_task_wait_to_begin_page(self):
    """
    到达任务未开始时界面
    """
    click_pos = [
        [995, 101],
        [1154, 659],
        [1154, 659],
        [1154, 659],
        [1154, 659],
    ]
    los = [
        "mission_info",
        "formation_edit1",
        "formation_edit2",
        "formation_edit3",
        "formation_edit4",
    ]
    ends = [
        "normal_task_wait_to_begin_page"
    ]
    color.common_rgb_detect_method(self, click_pos, los, ends)


def to_formation_edit_i(self, i, lo):
    """
    @param i: 编队编号
    @param lo: 进入配队界面需点击的位置
    到达编队页面
    """
    loy = [195, 275, 354, 423]
    y = loy[i - 1]
    click_pos = [
        [lo[0], lo[1]],
        [74, y],
        [74, y],
        [74, y],
        [74, y],
    ]
    los = [
        "normal_task_wait_to_begin_page",
        "formation_edit1",
        "formation_edit2",
        "formation_edit3",
        "formation_edit4",
    ]
    ends = [
        "formation_edit" + str(i)
    ]
    los.pop(i)
    click_pos.pop(i)
    color.common_rgb_detect_method(self, click_pos, los, ends)


def wait_over(self):
    """
    打开一次任务信息界面
    """
    click_pos1 = [
        [998, 670],
        [886, 162],
        [794, 207],
    ]
    lo1 = [
        "normal_task_mission_operating",
        "formation_teleport_notice",
        "present",
    ]
    end1 = ["normal_task_mission_info"]
    color.common_rgb_detect_method(self, click_pos1, lo1, end1)


def start_mission(self):
    """
    开始任务
    """
    possible = {
        'normal_task_fight-task': (1171, 670),
        'normal_task_task-begin-without-further-editing-notice': (768, 498),
        'normal_task_task-operating-round-over-notice': (888, 163)
    }
    image.detect(self, "normal_task_task-operating-feature", possible)
