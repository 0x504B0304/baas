stage_data = {
    '8-1': {
        'start': {
            '1': (612, 178),
            '2': (566, 693)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (710, 350), 'desc': "1 lower right"},
            {'t': 'move', 'ec': True, 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (650, 410), 'desc': "2 upper left"},
            {'t': 'move', 'ec': True, 'wo': True, 'desc': "teleport"},

            # 第二回合
            {'t': 'click', 'p': (617, 392), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (845, 475), 'ec': True, 'wo': True, 'desc': "1 lower right"},

            # 第三回合
            {'t': 'click', 'p': (555, 490), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (895, 425), 'wo': True, 'desc': "1 lower right"},

            # 第四回合
            {'t': 'click', 'p': (615, 395), 'ec': True, 'desc': "1 right & get box"},
            {'t': 'end-turn'},

            # 第四回合
            {'t': 'click', 'p': (615, 400), 'desc': "1 right"},
        ]
    },
    '8-1-box': '8-1',
    '8-1-task': {
        'start': {
            '1': (612, 178),
            '2': (566, 693)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (710, 350), 'desc': "1 lower right"},
            {'t': 'move', 'ec': True, 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (650, 410), 'desc': "2 upper left"},
            {'t': 'move', 'ec': True, 'wo': True, 'desc': "teleport"},

            # 第二回合
            {'t': 'click', 'p': (617, 392), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (845, 475), 'ec': True, 'wo': True, 'desc': "1 lower right"},

            # 第三回合
            {'t': 'click', 'p': (555, 490), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (720, 340), 'desc': "1 lower right"},
            {'t': 'move', 'ec': True, 'wo': True, 'desc': "teleport"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (630, 345), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (625, 345), 'desc': "choose 2"},
            {'t': 'click', 'p': (523, 336), 'desc': "change"},
            {'t': 'click', 'p': (743, 345), 'desc': "1 right"},
        ]
    },
    '8-2': {
        'start': {
            '1': (1000, 345),
            '2': (72, 373)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (725, 475), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (550, 475), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第二回合
            {'t': 'click', 'p': (665, 415), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (615, 440), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (555, 335), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (665, 405), 'wo': True, 'desc': "1 left"},

            # 第四回合
            {'t': 'click', 'p': (690, 550), 'desc': "1 lower left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (590, 235), 'ec': True, 'wo': True, 'desc': "2 upper right"},

            # 第五回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (610, 210), 'desc': "2 upper right"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'end-turn'},

            # 第六回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 1"},
            {'t': 'click', 'p': (435, 295), 'wo': True, 'desc': "2 left & get box"},
            {'t': 'click', 'p': (615, 480), 'desc': "1 lower left"},
        ]
    },
    '8-2-box': '8-2',
    '8-2-task': {
        'start': {
            '1': (1000, 345),
            '2': (72, 373)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (725, 475), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (550, 475), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第二回合
            {'t': 'click', 'p': (665, 415), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (615, 440), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (555, 335), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (665, 405), 'wo': True, 'desc': "1 left"},

            # 第四回合
            {'t': 'click', 'p': (690, 550), 'desc': "1 lower left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'end-turn'},

            # 第五回合
            {'t': 'click', 'p': (630, 465), 'desc': "1 lower left"},
        ]
    },
    '8-3': {
        'start': {
            '1': (790, 470),
            '2': (325, 320)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (555, 445), 'desc': "2 lower right"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (720, 340), 'desc': "choose 2"},
            {'t': 'click', 'p': (615, 335), 'desc': "change"},
            {'t': 'click', 'p': (775, 260), 'wo': True, 'desc': "1 upper right"},

            # 第二回合
            {'t': 'click', 'p': (720, 445), 'wo': True, 'desc': "2 lower right"},
            {'t': 'end-turn', 'wo': True},

            # 第三回合
            {'t': 'click', 'p': (560, 400), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (750, 415), 'wo': True, 'desc': "2 right"},

            # 第四回合
            {'t': 'click', 'p': (445, 265), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (890, 440), 'wo': True, 'desc': "2 right & get box"},

            # 第五回合
            {'t': 'click', 'p': (460, 250), 'wo': True, 'desc': "2 lower right"},
            {'t': 'end-turn', 'wo': True},

            # 第六回合
            {'t': 'click', 'p': (400, 300), 'wo': True, 'desc': "2 lower right"},
            {'t': 'end-turn'},
        ]
    },
    '8-3-box': '8-3',
    '8-3-task': {
        'start': {
            '1': (790, 470),
            '2': (325, 320)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (555, 445), 'desc': "2 lower right"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (720, 340), 'desc': "choose 2"},
            {'t': 'click', 'p': (615, 335), 'desc': "change"},
            {'t': 'click', 'p': (600, 340), 'wo': True, 'desc': "1 left"},

            # 第二回合
            {'t': 'click', 'p': (465, 245), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (820, 370), 'wo': True, 'desc': "2 upper right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (725, 310), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (520, 280), 'wo': True, 'desc': "2 upper left"},

            # 第四回合
            {'t': 'click', 'p': (430, 300), 'ec': True, 'desc': "1 upper left"},
            {'t': 'end-turn'},
        ]
    },
}
