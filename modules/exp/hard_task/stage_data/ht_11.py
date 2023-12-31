stage_data = {
    '11-1': {
        'start': {
            '1': (795, 470),
            '2': (865, 445)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (530, 425), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (650, 420), 'ec': True, "wait-over": True, "desc": "2 left"},

            # 第二回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (535, 420), "desc": "choose 1"},
            {'t': 'click', 'p': (430, 415), "desc": "change"},
            {'t': 'click', 'p': (475, 340), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (560, 430), 'wait-over': True, "desc": "1 left"},

            # 第三回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (570, 280), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (515, 360), "wait-over": True, "desc": "1 upper left"},

            # 第四回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (515, 200), "wait-over": True, "desc": "2 upper left & get box"},
            {'t': 'click', 'p': (450, 450), "desc": "1 left"},
        ]
    },
    '11-1-box': '11-1',
    '11-1-task': '11-1',
    '11-2': {
        'start': {
            '1': (395, 390),
            '2': (620, 560)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (570, 245), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (705, 415), "desc": "2 upper right"},
            {'t': 'move', "wait-over": True, "desc": "teleport"},

            # 第二回合
            {'t': 'click', 'p': (680, 190), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (655, 430), 'ec': True, "wait-over": True, "desc": "2 left"},

            # 第三回合
            {'t': 'click', 'p': (700, 285), 'ec': True, "wait-over": True, "desc": "1 right"},
            {'t': 'click', 'p': (700, 540), "wait-over": True, "desc": "2 lower left & get box"},

            # 第四回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (720, 420), 'ec': True, "wait-over": True, "desc": "2 upper right"},
            {'t': 'end-turn', "wait-over": True, },

            # 第五回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (665, 405), 'ec': True, "wait-over": True, "desc": "2 upper left"},
            {'t': 'click', 'p': (635, 370), "wait-over": True, "desc": "1 lower right"},

            # 第六回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (760, 365), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (760, 360), "desc": "choose 2"},
            {'t': 'click', 'p': (650, 360), "desc": "change"},
            {'t': 'click', 'p': (875, 375), "desc": "1 right"},
        ]
    },
    '11-2-box': '11-2',
    '11-2-task': {
        'start': {
            '1': (395, 390),
            '2': (620, 560)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (570, 245), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (705, 415), "desc": "2 upper right"},
            {'t': 'move', "wait-over": True, "desc": "teleport"},

            # 第二回合
            {'t': 'click', 'p': (680, 190), 'ec': True, "desc": "1 upper right"},
            {'t': 'click', 'p': (655, 430), 'ec': True, "wait-over": True, "desc": "2 left"},

            # 第三回合
            {'t': 'click', 'p': (700, 285), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (700, 375), 'ec': True, "wait-over": True, "desc": "2 upper left"},

            # 第四回合
            {'t': 'click', 'p': (650, 415), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (765, 410), 'ec': True, "wait-over": True, "desc": "2 upper left"},

            # 第五回合
            {'t': 'click', 'p': (765, 415), "desc": "choose 2"},
            {'t': 'click', 'p': (660, 405), "desc": "change"},
            {'t': 'click', 'p': (885, 415), 'ec': True, "desc": "1 right"},
        ]
    },
    '11-3': {
        'start': {
            '1': (790, 305),
            '2': (530, 490)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (820, 400), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (470, 370), "desc": "2 upper left"},
            {'t': 'move', "wait-over": True, "desc": "teleport"},

            # 第二回合
            {'t': 'click', 'p': (715, 505), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (630, 335), 'ec': True, "wait-over": True, "desc": "2 right"},

            # 第三回合
            {'t': 'click', 'p': (695, 550), "wait-over": True, "desc": "1 lower left & get box"},
            {'t': 'click', 'p': (670, 295), "desc": "2 right"},
        ]
    },
    '11-3-box': '11-3',
    '11-3-task': '11-3',
}
