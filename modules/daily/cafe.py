import threading
import time
from collections import defaultdict

import cv2
import numpy as np

from common import stage, ocr, image, position, color
from modules.baas import home

x = {
    'menu': (107, 9, 162, 36),
    '0.0': (1114, 642, 1155, 665),
    'students-arrived': (572, 240, 662, 269),
    'cafe-reward-status': (625, 135, 688, 171),
    'invitation-ticket': (421, 78, 451, 111),
    'inc-fav': (480, 596, 569, 636),  # 好感提升
}
preset_position = {
    1: (808, 263), 2: (808, 393), 3: (808, 533), 4: (812, 393), 5: (812, 523)
}


def to_cafe(self):
    possible = {
        'home_student': (89, 653),
        'cafe_cafe-reward-status': (905, 159),
        'cafe_invitation-ticket': (835, 97),
        'cafe_students-arrived': (922, 189),
        'cafe_inc-fav': (646, 437)
    }
    click_pos = [
        [1240, 577],
    ]
    los = ["gift"]
    ends = ["cafe"]
    return image.detect(self, 'cafe_menu', possible, pre_func=color.detect_rgb_one_time,
                        pre_argv=(self, click_pos, los, ends))


def start(self):
    # 回到首页
    home.go_home(self)
    # 进入咖啡厅
    to_cafe(self)
    # 领取收益
    get_cafe_money(self)
    # 邀请妹子
    invite_girl(self)
    if self.tc['config']['relationship_method'] == 'clear_furniture':
        # 初始化窗口
        init_window(self)
        # 和妹子互动
        start_interactive(self)
    elif self.tc['config']['relationship_method'] == 'present':
        positive_impress1(self)
    # 回到首页
    home.go_home(self)


def match(img):
    res = []
    for i in range(1, 4):
        template = position.iad["cafe_happy_face" + str(i)]
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        locations = np.where(result >= threshold)
        for pt in zip(*locations[::-1]):
            res.append([pt[0] + template.shape[1] / 2, pt[1] + template.shape[0] / 2 + 58])
    return res


def to_gift(self):
    click_pos = [
        [163, 639],
    ]
    los = ["cafe"]
    ends = ["gift"]
    color.common_rgb_detect_method(self, click_pos, los, ends)


def shot(self):
    time.sleep(1)
    self.latest_img_array = self.get_screenshot_array()


def positive_impress1(self):
    self.d().pinch_in()
    self.d.swipe(709, 558, 709, 209, duration=0.5)
    for i in range(0, 5):
        to_gift(self)
        t1 = threading.Thread(target=shot, args=(self,))
        t1.start()
        self.d.click(131, 660)
        self.d.swipe(131, 660, 1280, 660, duration=0.5)
        t1.join()
        res = match(self.latest_img_array)
        to_cafe(self)

        for j in range(0, len(res)):
            self.click(res[j][0], min(res[j][1], 591), wait=False)

        to_cafe(self)
        if i != 4:
            self.click(68, 636)
            time.sleep(1)
            self.click(1169, 90)
            time.sleep(1)


def start_interactive(self):
    preset = self.tc['config']['blank_preset']
    load_preset(self, preset)
    # 收起菜单
    time.sleep(0.2)
    self.double_click(555, 622, False)
    i = 3
    while i > 0:
        click_girl_plus(self, i)
        if ocr.screenshot_check_text(self, '好感等级提升', (473, 593, 757, 644), 3):
            # 关闭好感窗口,重新开始
            self.double_click(651, 285, False)
            time.sleep(0.5)
            i = 3
            continue
        i -= 1
    # 暂开菜单
    self.click(57, 624, False)
    # 恢复玩家原有预设
    recover_preset(self, preset)


def recover_preset(self, preset):
    # 恢复玩家原有预设
    open_preset_window(self, preset)
    self.click(*preset_position[preset], False)
    confirm_load_preset(self)


def load_preset(self, preset):
    open_preset_window(self, preset)
    # 保存当前配置到配置中预设
    save_preset(self, preset)
    # 点击全部收纳
    self.click(455, 642, False, 1, 0.5)
    # 等待确认加载
    ocr.screenshot_check_text(self, '确认', (732, 482, 803, 518))
    # 确认收纳
    self.click(769, 498, False)


def open_preset_window(self, preset):
    # 等待右下角预设
    ocr.screenshot_check_text(self, '预设', (326, 656, 366, 677))
    # 点击右下角预设
    self.click(360, 640)
    # 等待预设弹窗加载
    ocr.screenshot_check_text(self, '预设', (604, 127, 678, 157))
    if preset > 3:
        self.swipe(933, 586, 933, 230)
        time.sleep(0.5)


def create_blank_preset(self, preset):
    # 把当前配置保存到空白预设
    save_preset(self, preset)
    # 点击全部收纳
    self.click(455, 642, False, 1, 0.5)
    # 等待确认加载
    ocr.screenshot_check_text(self, '确认', (732, 482, 803, 518))
    # 确认收纳
    self.click(769, 498, False)
    # 重新打开预设
    open_preset_window(self, preset)
    # 保存预设
    save_preset(self, preset)
    # 等待加载
    ocr.screenshot_check_text(self, '制造工坊', (732, 482, 803, 518), 0, 0, False)
    # 点击确认
    self.click(769, 498, False)


def save_preset(self, preset):
    area = preset_position[preset]
    # 点击保存当前配置
    self.click(area[0] - 250, area[1], False)
    # 确认加载预设
    confirm_load_preset(self)


def confirm_load_preset(self):
    # 等待加载
    ocr.screenshot_check_text(self, '确认', (732, 482, 803, 518))
    # 确认加载
    self.click(771, 500, False)
    # 等待预设弹窗加载
    ocr.screenshot_check_text(self, '预设', (604, 127, 678, 157))
    # 关闭预设
    self.double_click(934, 146, False)


def init_window(self):
    # 双指捏合
    sx1, sy1 = 1000, 330
    sx2, sy2 = 800, 330
    ex1, ey1 = 150, 330
    ex2, ey2 = 150, 330
    self.d().gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))
    # 拖到最左边
    self.swipe(392, 564, 983, 82)


def to_invitation_ticket(self):
    possible = {
        'cafe_cafe-reward-status': (905, 159),
        'cafe_menu': (838, 647),
    }
    return image.detect(self, 'cafe_invitation-ticket', possible)


def invite_girl(self):
    if not ocr.screenshot_check_text(self, "可以使用", (801, 586, 875, 606), 0):
        return
    # 邀请
    if 'priority' not in self.tc['config']:
        self.exit("配置文件版本太旧，请更换此功能的配置代码为最新版本")
    target_name_list = self.tc['config']['priority']
    self.logger.info("inviting" + str(target_name_list))
    for i in range(0, len(target_name_list)):
        t = ""
        for j in range(0, len(target_name_list[i])):
            if target_name_list[i][j] == '(' or target_name_list[i][j] == "（" or target_name_list[i][j] == ")" or \
                    target_name_list[i][j] == "）":
                continue
            else:
                t = t + target_name_list[i][j]
        target_name_list[i] = t
    f = True
    for i in range(0, len(target_name_list)):
        to_invitation_ticket(self)
        target_name = target_name_list[i]
        self.logger.info("begin find student " + target_name)
        swipe_x = 630
        swipe_y = 580
        dy = 430
        student_name = ["瞬(小)", "桐乃", "纱绫(便服)", "日富美(泳装)", "真白(泳装)", "鹤城(泳装)",
                        "白子(骑行)" "梓(泳装)", "爱丽丝", "切里诺", "志美子", "日富美", "佳代子",
                        "明日奈", "菲娜", "艾米", "真纪",
                        "泉奈", "明里", "芹香", "优香", "小春",
                        "花江", "纯子", "千世", "干世", "莲见", "爱理", "睦月", "野宫", "绫音", "歌原",
                        "芹娜", "小玉", "铃美", "朱莉", "好美", "千夏", "琴里",
                        "春香", "真白", "鹤城", "爱露", "晴奈", "日奈", "伊织", "星野",
                        "白子", "柚子", "花凛", "妮露", "纱绫", "静子", "花子", "风香",
                        "和香", "茜", "泉", "梓", "绿", "堇", "瞬", "桃", "椿", "晴", "响"]
        for i in range(0, len(student_name)):
            t = ""
            for j in range(0, len(student_name[i])):
                if student_name[i][j] == '(' or student_name[i][j] == "（" or student_name[i][j] == ")" or \
                        student_name[i][j] == "）":
                    continue
                else:
                    t = t + student_name[i][j]
            student_name[i] = t
        stop_flag = False
        last_student_name = None
        while not stop_flag:
            img_shot = self.get_screenshot_array()
            out = self.ocrChinese.ocr(img_shot)
            detected_name = []
            location = []
            for i in range(0, len(out)):
                for j in range(0, len(student_name)):
                    if len(detected_name) <= 4:
                        t = out[i]['text']
                        res = ""
                        for x in range(0, len(t)):
                            if t[x] == '(' or t[x] == "（" or t[x] == ")" or t[x] == "）":
                                continue
                            else:
                                res = res + t[x]
                        if res == student_name[j]:
                            if student_name[j] == "干世":
                                detected_name.append("千世")
                            else:
                                detected_name.append(student_name[j])
                            location.append(out[i]['position'][0][1] + 25)
                    else:
                        break
            if len(detected_name) == 0:
                self.logger.info("No name detected")
                break
            st = ""
            for i in range(0, len(detected_name)):
                st = st + detected_name[i] + " "
            self.logger.info("detected name :" + st)
            if detected_name[len(detected_name) - 1] == last_student_name:
                self.logger.warning("Can't detect target student")
                stop_flag = True
            else:
                last_student_name = detected_name[len(detected_name) - 1]
                for s in range(0, len(detected_name)):
                    if detected_name[s] == target_name:
                        self.logger.info("find student " + target_name + " at " + str(location[s]))
                        stop_flag = True
                        f = False
                        self.click(784, location[s], wait=False)
                        time.sleep(0.7)
                        self.click(770, 500)
                        break
                if not stop_flag:
                    self.logger.info("didn't find target student swipe to next page")
                    self.d.swipe(swipe_x, swipe_y, swipe_x, swipe_y - dy, duration=0.5)
                    self.click(617, 500)
        to_cafe(self)
        if not f:
            break


def get_cafe_money(self):
    # 查看是否需要领取体力
    if not self.tc['config']['receive_ap']:
        return
    # 查看收益
    if image.compare_image(self, 'cafe_0.0', 0):
        return
    # 点击咖啡厅收益
    self.click(1155, 645)
    # 等待领取
    ocr.screenshot_check_text(self, "领取", (600, 500, 678, 538))
    # 点击领取
    self.click(641, 516)
    # 关闭获得奖励
    stage.close_prize_info(self, True)
    # 关闭领取界面
    self.click(903, 155, False)
    # 防止体力超出
    self.click(903, 155, False)


def click_girl_plus(self, i):
    if i % 2 == 0:
        self.swipe(327, 512, 1027, 125)
    else:
        self.swipe(1008, 516, 300, 150)
    time.sleep(0.5)
    before = self.d.screenshot()
    time.sleep(1)
    after = self.d.screenshot()
    # 将图像转换为numpy数组以便进行数学操作
    img1_data = np.array(before)
    img2_data = np.array(after)

    diff_pixels_coords = np.where(img1_data != img2_data)
    # 创建一个映射，键是每个像素点所在的50px区块的坐标，值是该区块中所有不同像素点的列表
    blocks = defaultdict(list)

    for p in zip(*diff_pixels_coords):
        x = int(p[1])
        y = int(p[0])
        # 计算此像素所在的区块坐标
        block_coord = (y // 50, x // 50)
        blocks[block_coord].append((y, x))

    # 对于每个区块，保留中间的像素点
    finial = []
    for block_coord, pixels in blocks.items():
        # 将像素列表按照Y和X排序
        pixels.sort()
        # 取出中间的像素
        mid_pixel = pixels[len(pixels) // 2]
        # 将坐标变换回原图尺寸
        center_coord = (mid_pixel[0] * 1 + 0.5, mid_pixel[1] * 1 + 0.5)
        # 防止溢出到功能按钮
        x = int(center_coord[1])
        y = int(center_coord[0])
        if y < 70 or \
                (y < 130 and x < 320) or (y < 130 and x > 1170) or \
                (y > 570 and x < 100) or (y > 570 and x > 770):
            continue
        finial.append(center_coord)
    # 打乱坐标
    np.random.shuffle(finial)
    for p in finial:
        self.click(int(p[1]), int(p[0]), False)
