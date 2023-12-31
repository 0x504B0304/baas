stage_data = {
    '14-1': {
        'start': {
            '1': (550, 305),
            '2': (581, 686)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (785, 275), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (715, 500), 'ec': True, "wait-over": True, "desc": "2 right"},

            # 第二回合
            {'t': 'click', 'p': (780, 375), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (715, 420), 'ec': True, "wait-over": True, "desc": "2 upper right"},

            # 第三回合
            {'t': 'click', 'p': (895, 340), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (665, 365), 'ec': True, "wait-over": True, "desc": "2 upper right"},

            # 第四回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (412, 322), 'ec': True, "desc": "2 left"},
            {'t': 'click', 'p': (760, 405), "wait-over": True, "desc": "1 lower right"},

            # 第五回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (450, 420), "wait-over": True, "desc": "2 lower left & get box"},
            {'t': 'click', 'p': (715, 515), "desc": "1 lower left"},
        ]
    },
    '14-1-box': '14-1',
    '14-1-task': '14-1',
    '14-2': {
        'start': {
            '1': (875, 305),
            '2': (475, 585)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (690, 390), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (605, 395), 'ec': True, "wait-over": True, "desc": "2 upper right"},

            # 第二回合
            {'t': 'click', 'p': (640, 320), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (643, 323), "desc": "choose 1"},
            {'t': 'click', 'p': (540, 320), "desc": "change"},
            {'t': 'click', 'p': (580, 235), "wait-over": True, "desc": "2 upper left"},

            # 第三回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (520, 275), 'ec': True, "desc": "2 left"},
            {'t': 'click', 'p': (565, 445), "wait-over": True, "desc": "1 left"},

            # 第四回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (620, 200), "wait-over": True, "desc": "2 upper left & get box"},
            {'t': 'click', 'p': (575, 425), "desc": "1 upper left"},
        ]
    },
    '14-2-box': '14-2',
    '14-2-task': '14-2',
    '14-3': {
        'start': {
            '1': (875, 345),
            '2': (425, 200)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (655, 430), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (460, 405), 'ec': True, "wait-over": True, "desc": "2 lower left"},

            # 第二回合
            {'t': 'click', 'p': (630, 465), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (550, 465), 'ec': True, "wait-over": True, "desc": "2 lower right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (625, 460), 'ec': True, "desc": "2 lower right"},
            {'t': 'click', 'p': (625, 460), "desc": "choose 2"},
            {'t': 'click', 'p': (520, 455), "desc": "change"},
            {'t': 'click', 'p': (565, 545), "wait-over": True, "desc": "1 lower left"},

            # 第四回合
            {'t': 'click', 'p': (390, 435), "wait-over": True, "desc": "1 left & get box"},
            {'t': 'click', 'p': (825, 250), "desc": "2 upper right"},
        ]
    },
    '14-3-box': '14-3',
    '14-3-task': '14-3',
}
