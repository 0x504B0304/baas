import importlib
import time

import cv2
import numpy as np

from common import ocr, color, image, stage
from modules.attack import normal_task
from modules.baas import home
from modules.story import main_story

# 普通关卡坐标
normal_position = {
    1: (1120, 240), 2: (1120, 340), 3: (1120, 440), 4: (1120, 540), 5: (1120, 568),
}
# 部队1234坐标
force_position = {
    1: (124, 195), 2: (124, 277), 3: (124, 354), 4: (124, 429),
}


def to_end_over(self):
    pos = {
        'fight_tasking': (1172, 668),
    }
    image.detect(self, 'fight_confirm', pos)


def to_task_menu(self):
    possible = {
        'fight_pass-confirm': (1170, 666),
        'fight_task-finish-confirm': (1033, 666),
        'fight_prize-confirm': (776, 655),
    }
    image.detect(self, 'normal_task_choose-region', possible, ss_rate=2)
    stage.wait_loading(self)


def to_force_edit_page(self, x):
    """
    回到任部队编辑界面
    :param self:
    :param x:
    :return:
    """
    pos = {
        'fight_start-task': x,  # 任务开始界面
    }
    image.detect(self, 'fight_force-edit', pos)


def to_tart_task_page(self):
    time.sleep(0.5)
    """
    回到任务开始或任务中
    :param self:
    :return:
    """
    pos = {
        'fight_confirm': (770, 500),  # 确认信息
        'fight_fighting-task-info': (520, 20),  # 任务信息->关闭
        'fight_force-edit': (1162, 658),  # 部队编辑界面
        'normal_task_get-box': (520, 20),  # 领取宝箱->关闭
    }
    image.detect(self, ('fight_start-task', 'fight_tasking'), pos)


def start(self):
    # 回到首页
    home.go_home(self)
    # 到选择任务区域
    normal_task.to_choose_region(self)
    # 选择任务模式
    normal_task.change_task(self)

    # 获取开图数据
    region = self.tc['config']['region']
    self.stage_data = get_stage_data(self, region)
    if self.stage_data is None:
        return home.go_home(self)
    # 开始战斗
    start_fight(self, region)
    # 回到首页
    home.go_home(self)


def start_task(self):
    pos = {
        'normal_task_task-info-window': (947, 540)  # 任务信息 -> 开始任务
    }
    image.detect(self, 'fight_start-task', pos)


def start_fight(self, region, gk=None):
    # 选择区域
    gk_none = gk is None
    if gk_none:
        # 选择区域
        normal_task.choose_region(self, region)
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
        # todo 这里可以优化
        self.click(947, 540)
    # 等待地图加载

    # 遍历start需要哪些队伍
    if gk == "side":
        # 选择支线部队开始战斗
        start_choose_side_team(self)
        image.compare_image(self, 'fight_force-edit')
        image.compare_image(self, 'fight_force-edit', threshold=0.6, mis_fu=self.click, mis_argv=(1171, 670),
                            rate=1,
                            n=True)
    else:
        starts = get_gk_data(gk, self.stage_data, 'start')
        for n, p in starts.items():
            start_choose_team(self, gk, n)
        # 点击开始任务
        start_mission(self)
        # 检查跳过战斗
        check_skip_auto_over(self)
        # 开始走格子
        start_action(self, gk, self.stage_data)
    # 自动战斗
    main_story.auto_fight(self)
    self.logger.info("强制等待25秒...")
    time.sleep(25)
    to_task_menu(self)
    # 返回上一个区域,防止解锁地图卡识别
    normal_task.choose_region(self, region - 1)
    # 重新开始本区域探索
    if gk_none:
        return start_fight(self, region)


def check_skip_auto_over(self):
    # 检查跳过战斗
    image.compare_image(self, 'fight_skip-fight', threshold=0.6, mis_fu=self.click, mis_argv=(1123, 545),
                        rate=2)
    # 检查回合自动结束
    image.compare_image(self, 'fight_auto-over', threshold=0.6, mis_fu=self.click, mis_argv=(1082, 599),
                        rate=2)


def get_stage_data(self, region):
    # 动态生成完整的模块路径
    if 'hard_task' in self.tc['task']:
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
    # 主线-未通关 todo 游戏维护没拿到位置
    star_position = {
        'cn': (211, 368),
        'intl': (211, 368),
        'jp': (211, 368),
    }
    # 未通关
    if color.check_rgb(self, star_position[self.game_server], (202, 204, 202)):
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
        if image.compare_image(self, 'normal_task_task-info-window', 0):
            return 'main'
        # 支线任务
        if image.compare_image(self, 'normal_task_side-quest', 0):
            return 'side'
        time.sleep(0.1)
        # 是否要打开入场
        if open_task:
            # 不是国服需要重置关卡顺序
            if self.tc['task'] == 'exp_normal_task':
                stage.screen_swipe(self, 0, 0)
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
    stage_index = 1
    while True:
        # 等待任务信息加载
        task_state = check_task_state(self)
        self.logger.warning("当前关卡状态为:{0}".format(task_state))
        # 未通关支线
        if task_state == 'side':
            self.logger.warning("未通关支线，开始支线战斗")
            return task_state
        # 获取当前关卡
        current_stage = get_stage(self, region, task_state, stage_index)
        # 未通关主线
        if task_state == 'no-pass':
            self.logger.warning(f"{current_stage} 未通关主线，开始主线战斗")
            return current_stage
        # 模式2 ⭐️⭐️⭐️  或者 ⭐️⭐️⭐️+宝箱礼物
        if self.tc['config']['mode'] == 2:
            if task_state == 'box':
                self.logger.warning(f"{current_stage} 发现星辉石宝箱，开始主线战斗")
                return current_stage
            if task_state != 'sss':
                self.logger.warning(f"{current_stage} 未三星通关，开始主线战斗")
                return current_stage
        # 点击下一关
        self.logger.warning(f"{current_stage} 不满足战斗条件,查找下一关")
        self.click(1172, 358)
        # 检测是否还在本区域
        stage_index += 1
        mc = 4 if self.tc['task'] == 'exp_hard_task' else 6
        if stage_index >= mc:
            time.sleep(1)
            if region != ocr.screenshot_get_text(self, (189, 197, 228, 225), self.ocrNum):
                return None


def get_stage(self, region, task_state, stage_index):
    s = '{0}-{1}'.format(region, stage_index)
    if task_state == 'box':
        return s + '-box'
    return s
    # max = 7 if self.game_server != 'cn' and region in [6, 9, 12, 15, 18] else 6
    # for i in range(1, max):
    #     s = '{0}-{1}'.format(region, i)
    #     try:
    #         box = (191, 199, 265, 224) if self.game_server == 'cn' else (146, 199, 219, 229)
    #         if image.compare_image(self, 'normal_task_' + s, 0, box=box):
    #             if task_state == 'box':
    #                 return s + '-box'
    #             return s
    #     except KeyError:
    #         self.logger.critical("当前关卡{0}尚未支持开图，正在全力研发中...".format(s))
    #         return None
    # return None


def get_force(self):
    """
    获取左下角部队编号
    由于ocr将1识别为7,所以7都识别为1
    """
    self.latest_img_array = cv2.cvtColor(np.array(self.d.screenshot()), cv2.COLOR_RGB2BGR)
    x1, x2, y1, y2 = 116, 131, 542, 570
    if self.game_server == 'intl':
        x1, x2, y1, y2 = 75, 92, 550, 566
    img = self.latest_img_array[y1:y2, x1:x2]
    ocr_res = self.ocrNum.ocr_for_single_line(img)["text"]
    if ocr_res == "":
        return get_force(self)
    if ocr_res == "7":
        return 1
    return int(ocr_res)


def start_action(self, gk, stage_data):
    actions = get_gk_data(gk, stage_data, 'action')
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
            to_tart_task_page(self)
        elif act['t'] == 'end-turn':
            self.logger.info("结束回合")
            to_end_over(self)
            to_tart_task_page(self)
        elif act['t'] == 'get-box':
            self.logger.info("领取宝箱")
            to_tart_task_page(self)
        # 判断是否存在exchange事件
        if 'ec' in act:
            # 等待换队
            self.logger.info("等待队伍更换事件...")
            origin = force_index
            while force_index == origin:
                force_index = get_force(self)
                time.sleep(0.5)
        # 判断是否存在wait over事件
        if 'wo' in act:
            self.logger.info("等待战斗结束...")
            wait_over(self)
            to_tart_task_page(self)
        # 行动后置等待时间
        if 'after' in act:
            self.logger.info("后置等待{0}秒".format(act['after']))
            time.sleep(act['after'])

    self.logger.warning("行动结束,等待进入战斗...")
    image.compare_image(self, 'fight_tasking', n=True, rate=1)


def get_gk_data(gk, stage_data, attr):
    gk_data = stage_data[gk]
    if type(gk_data) is str:
        return stage_data[gk_data][attr]
    return gk_data[attr]


def start_choose_team(self, gk, force):
    start_task(self)
    # 到部队编辑页面
    starts = get_gk_data(gk, self.stage_data, 'start')
    to_force_edit_page(self, starts[force])
    # 选择对应属性的队伍
    select_force_fight(self, force)
    # 回到任务开始界面
    to_tart_task_page(self)


def choose_team_and_start_action(self, gk):
    starts = get_gk_data(gk, self.stage_data, 'start')
    for n, p in starts.items():
        start_choose_team(self, gk, n)
    # 点击开始任务
    start_mission(self)
    # 检查跳过战斗
    check_skip_auto_over(self)
    # 开始走格子
    start_action(self, gk, self.stage_data)


def start_choose_side_team(self):
    # 选择对应属性的队伍
    select_force_fight(self, 1)


def select_force_fight(self, index):
    """
    选择队伍并开始战斗
    @param self:
    @param index: 队伍索引
    """
    index = int(index)
    self.logger.info("选择部队{0}".format(index))
    fp = force_position[index]
    # 检查是否有选中,直到选中为止
    while not color.check_rgb(self, fp, (45, 70, 99)):
        self.click(*fp)
        time.sleep(self.bc['baas']['base']['ss_rate'])


def wait_over(self):
    # 打开任务信息
    image.detect(self, 'fight_fighting-task-info', cl=(996, 666), ss_rate=1)


def start_mission(self):
    """
    开始任务
    """
    time.sleep(0.5)
    pos = {
        'fight_start-task': (1171, 670),  # 开始任务
        'fight_confirm': (770, 500),  # 确认信息
    }
    image.detect(self, 'fight_tasking', pos)
