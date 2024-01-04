import time

from common import image, stage, color
from modules.baas import home
from modules.exp.normal_task import exp_normal_task
from modules.scan import main_story

position = {
    9: (1130, 185), 10: (1130, 300), 11: (1130, 420), 12: (1130, 430)
}

stage_data = {
    'task-4': {
        'start': {
            '1': (793, 427),
        },
        'action': [
            {'t': 'click', 'p': (808, 338), 'wo': True},
            {'t': 'click', 'p': (724, 311), 'wo': True},
            {'t': 'click', 'p': (664, 378), 'wo': True},
            {'t': 'click', 'p': (648, 490), 'wo': True},
            {'t': 'click', 'p': (581, 576)},
        ]
    },
    'task-8': {
        'start': {
            '1': (405, 390),
            '2': (970, 230),
        },
        'action': [
            {'t': 'click', 'p': (625, 430), 'ec': True},
            {'t': 'click', 'p': (655, 340), 'wo': True},
            {'t': 'click', 'p': (555, 315), 'ec': True},
            {'t': 'click', 'p': (660, 235), 'wo': True},
            {'t': 'click', 'p': (705, 335), 'ec': True},
            {'t': 'click', 'p': (555, 275)},
        ]
    },
    'task-12': {
        'start': {
            '1': (580, 430),
            '2': (585, 150),
        },
        'action': [
            {'t': 'click', 'p': (730, 430), 'ec': True},
            {'t': 'click', 'p': (675, 360), 'wo': True},
            {'t': 'click', 'p': (760, 440), 'ec': True},
            {'t': 'click', 'p': (645, 440), 'wo': True},
            {'t': 'click', 'p': (785, 270), 'ec': True},
            {'t': 'click', 'p': (405, 460)},
        ]
    },
    'challenge-2': {},
    'challenge-4': {},
}


def start(self):
    if self.game_server != 'cn':
        return
    # 回到首页
    home.go_home(self)
    to_activity_page(self)
    # 开图
    if self.tc['exp']['enable']:
        start_exp(self)
    # 扫荡
    if self.tc['scan']['enable']:
        start_scan(self)
    # 回到首页
    home.go_home(self)


def start_scan(self):
    to_tab(self, 'task')
    stage_list = self.tc['scan']['stage']
    stage_list = sorted(stage_list, key=lambda x: int(x.split('-')[1]))
    stage.screen_swipe(self, threshold2=0, reset=False, f=(926, 590, 926, 0, 0.1))
    for task in stage_list:
        gq, count = task.split('-')
        gq = int(gq)
        self.click(*position[gq])
        # 确认扫荡
        rst = stage.confirm_scan(self, gq, count, 99)
        if rst == 'return':
            return
        to_activity_page(self)


def to_tab(self, t):
    """
    到指定tab页面
    @param self:
    @param t:
    """
    tabs = {
        'story': ((832, 103, 833, 104), (77, 55, 40)),
        'task': ((1002, 103, 1003, 104), (77, 55, 40)),
        'challenge': ((1190, 103, 1191, 104), (77, 55, 40))
    }
    tab = tabs[t]
    color.wait_rgb_similar(self, tab[0], tab[1], cl=(tab[0][0] - 100, tab[0][1]))


def to_activity_page(self):
    """
    到活动页面
    @param self:
    """
    pos = {
        'home_student': (1192, 204),  # 首页活动入口
        'momo_talk_menu': (1205, 42),  # 桃信菜单
        'momo_talk_skip': (1212, 116),  # 桃信跳过
        'momo_talk_confirm-skip': (770, 516),  # 桃信确认跳过
        'normal_task_task-info': (1084, 142),  # 任务信息
        'spa_227_guide': (1184, 156),  # 活动玩法指引
    }
    image.detect(self, 'spa_227_menu', pos, ss_rate=2)


def start_exp(self):
    """
    开始开图
    @param self:
    """
    tabs = ['story', 'task']
    # tabs = ['story', 'task', 'challenge']
    for tab in tabs:
        to_activity_page(self)
        do_exp(self, tab)


def do_exp(self, tab):
    """
    执行开图
    @param self:
    @return:
    """
    to_tab(self, 'challenge')
    to_activity_page(self)
    to_tab(self, tab)
    state, stage_index = calc_need_fight_stage(self)
    if state is None:
        self.logger.critical("本区域没有需要开图的任务关卡...")
        return
    # 支线和主线点击不同位置
    pos = {
        'main_story_main-lv-start-task': (943, 532),
        'main_story_side-lv-start-task': (640, 511),
    }
    ends = (
        'momo_talk_menu', 'normal_task_force-edit', 'momo_talk_skip', 'momo_talk_confirm-skip',
        'fight_start-task')
    end = image.detect(self, ends, pos)
    if end == 'fight_start-task':
        # 出击F
        gk = f'{tab}-{stage_index}'
        if gk not in stage_data:
            image.compare_image(self, 'fight_force-edit')
            image.compare_image(self, 'fight_force-edit', threshold=0.6, cl=(1171, 670), rate=1, n=True)
        else:
            self.stage_data = stage_data
            starts = exp_normal_task.get_gk_data(gk, self.stage_data, 'start')
            for n, p in starts.items():
                exp_normal_task.start_choose_team(self, gk, n)
            # 点击开始任务
            exp_normal_task.start_mission(self)
            # 检查跳过战斗
            exp_normal_task.check_skip_auto_over(self)
            # 开始走格子
            exp_normal_task.start_action(self, gk, self.stage_data)
    else:
        # 跳过剧情
        skip_story(self)
        # 出击
        image.compare_image(self, 'fight_force-edit')
        image.compare_image(self, 'fight_force-edit', threshold=0.6, cl=(1171, 670), rate=1, n=True)
    # 自动战斗
    main_story.auto_fight(self)
    self.logger.info("强制等待25秒...")
    time.sleep(25)
    # 等待战斗结束
    possible = {
        'main_story_fight-confirm': (1168, 659),  # 战斗通过
        'main_story_fight-fail': (647, 655),  # 战斗失败

        'fight_pass-confirm': (1170, 666),  # 战斗成功第一次确认
        'fight_task-finish-confirm': (1033, 666),  # 战斗成功第二次确认(任务完成)
        'fight_prize-confirm': (776, 655),  # 获得奖励确认按钮(支线通关)
        'fight_prize-confirm2': (645, 670),  # 获得奖励确认按钮2

        'momo_talk_menu': (1205, 42),  # 剧情菜单
        'momo_talk_skip': (1212, 116),  # 剧情跳过
        'momo_talk_confirm-skip': (770, 516),  # 剧情确认跳过

        'spa_227_unlock': (1259, 62),  # 解锁道具

    }
    image.detect(self, 'spa_227_menu', possible)
    do_exp(self, tab)


def skip_story(self):
    """
    跳过剧情到部队编辑界面
    """
    pos = {
        'momo_talk_menu': (1205, 42),
        'momo_talk_skip': (1212, 116),
        'momo_talk_confirm-skip': (770, 516),
    }
    image.detect(self, 'normal_task_force-edit', pos)


def wait_task_info(self, open_info=True):
    """
    等待任务信息加载
    @param open_info: 打开任务信息
    @param self:
    """
    if open_info:
        image.detect(self, ('normal_task_task-info', 'normal_task_side-quest'), cl=(1082, 190))
    else:
        image.compare_image(self, 'normal_task_task-info', 10)


def calc_need_fight_stage(self):
    """
    查找需要战斗的关卡
    @param self:
    @return:
    """
    wait_task_info(self)
    stage_index = 1
    while True:
        # 等待任务信息加载
        task_state = check_task_state(self)
        self.logger.info("当前关卡状态为:{0}".format(task_state))
        if task_state == 'sss':
            # 点击下一关
            self.logger.warn("不满足战斗条件,查找下一关")
            self.click(1172, 358)
            stage_index += 1
            continue
        elif task_state is None:
            return None, 0
        return task_state, stage_index
    return None, 0


def check_task_state(self):
    """
    检查任务当前类型
    @param self:
    @return:
    """
    # 等待任务信息弹窗加载
    wait_task_info(self, False)
    time.sleep(1)
    # 三星
    if image.compare_image(self, 'normal_task_sss', 0):
        return 'sss'
    # 没关卡了
    if image.compare_image(self, 'spa_227_menu', 0):
        return None
    return 'no-sss'
