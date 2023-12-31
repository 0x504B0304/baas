stage_data = {
    '12-1': {
        'start': {
            '1': (335, 555),
            '2': (1130, 455)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (610, 395), 'wo': True, 'desc': "1 right"},
            {'t': 'click', 'p': (665, 390), 'wo': True, 'desc': "2 left"},

            # 第二回合
            {'t': 'click', 'p': (550, 310), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (725, 315), 'ec': True, 'wo': True, 'desc': "2 upper left"},

            # 第三回合
            {'t': 'click', 'p': (560, 345), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (680, 510), 'ec': True, 'wo': True, 'desc': "2 lower left"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (555, 505), 'wo': True, 'desc': "2 left & get box"},
            {'t': 'click', 'p': (510, 250), 'desc': "1 upper left"},
        ]
    },
    '12-1-box': '12-1',
    '12-1-task': '12-1',
    '12-2': {
        'start': {
            '1': (365, 385),
            '2': (620, 390)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (578, 475), 'wo': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (585, 480), 'desc': "choose 1"},
            {'t': 'click', 'p': (478, 468), 'desc': "change"},
            {'t': 'click', 'p': (640, 560), 'wo': True, 'desc': "2 lower right"},

            # 第二回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (785, 485), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (685, 235), 'wo': True, 'desc': "1 upper right"},

            # 第三回合
            {'t': 'click', 'p': (745, 270), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (800, 500), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (640, 415), 'wo': True, 'desc': "2 upper left & get box"},
            {'t': 'click', 'p': (730, 275), 'desc': "1 right"},
        ]
    },
    '12-2-box': '12-2',
    '12-2-task': '12-2',
    '12-3': {
        'start': {
            '1': (610, 385),
            '2': (580, 305)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (760, 390), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (760, 390), 'desc': "choose 2"},
            {'t': 'click', 'p': (660, 380), 'desc': "change"},
            {'t': 'click', 'p': (815, 310), 'desc': "2 upper right"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},

            # 第二回合
            {'t': 'click', 'p': (895, 400), 'wo': True, 'desc': "1 right & get box"},
            {'t': 'end-turn', 'wo': True},

            # 第三回合
            {'t': 'click', 'p': (730, 310), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (505, 390), 'ec': True, 'wo': True, 'desc': "2 lower left"},

            # 第四回合
            {'t': 'click', 'p': (705, 250), 'desc': "1 upper left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (725, 595), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第五回合
            {'t': 'click', 'p': (455, 290), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (605, 485), 'ec': True, 'wo': True, 'desc': "2 left"},

            # 第六回合
            {'t': 'click', 'p': (495, 380), 'desc': "1 lower left"}
        ]
    },
    '12-3-box': '12-3',
    '12-3-task': {
        'start': {
            '1': (610, 385),
            '2': (580, 305)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (760, 390), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (760, 390), 'desc': "choose 2"},
            {'t': 'click', 'p': (660, 380), 'desc': "change"},
            {'t': 'click', 'p': (815, 310), 'desc': "2 upper right"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},

            # 第二回合
            {'t': 'click', 'p': (830, 315), 'desc': "1 upper right"},
            {'t': 'end-turn', 'wo': True},

            # 第三回合
            {'t': 'click', 'p': (710, 255), 'desc': "1 upper left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'end-turn', 'wo': True},

            # 第四回合
            {'t': 'click', 'p': (400, 335), 'desc': "1 left"},
            {'t': 'end-turn', 'wo': True},

            # 第五回合
            {'t': 'click', 'p': (465, 400), 'ec': True, 'desc': "1 lower left"},
        ]
    },
}
