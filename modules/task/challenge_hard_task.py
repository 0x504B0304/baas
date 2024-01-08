import time

from common import image
from modules.attack import normal_task, hard_task
from modules.baas import home
from modules.exp.normal_task import exp_normal_task
from modules.story import main_story


def start(self):
    # 回到首页
    home.go_home(self)
    # 到选择任务区域
    normal_task.to_choose_region(self)
    # 选择任务模式
    normal_task.change_task(self)

    stage_list = self.tc['scan']['stage']
    for task in stage_list:
        gk = task + '-task'
        region, stage = task.split('-')
        self.stage_data = exp_normal_task.get_stage_data(self, region)
        if gk not in self.stage_data:
            self.logger.critical("本关卡{0}尚未支持挑战任务，正在全力研发中...".format(gk))
            continue
        normal_task.choose_region(self, int(region))
        # 选择关卡
        normal_task.open_task_info_window(self, hard_task.hard_position[int(stage)])
        # 检查关卡状态
        state = check_stage(self)
        if state == 'continue':
            continue
        elif state == 'break':
            break
        # 选择队伍并开始行动
        exp_normal_task.choose_team_and_start_action(self, gk)
        # 自动战斗
        main_story.auto_fight(self)
        self.logger.info("强制等待25秒...")
        time.sleep(25)
        exp_normal_task.to_task_menu(self)

    # 回到首页
    home.go_home(self)


def check_stage(self):
    ends = (
        'normal_task_buy-hard-count',  # 困难次数不足
        'normal_task_buy-ap-window',  # 购买体力弹窗
        'fight_start-task',  # 战斗中-开始任务
    )
    pos = {
        'normal_task_task-info-window': (947, 540)  # 任务信息 -> 开始任务
    }
    end = image.detect(self, ends, pos)
    if end == 'normal_task_buy-hard-count':
        home.click_house_under(self)
        return 'continue'
    elif end == 'normal_task_buy-ap-window':
        return 'break'
    return 'ok'
