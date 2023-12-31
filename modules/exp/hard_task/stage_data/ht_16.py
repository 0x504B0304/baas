stage_data = {
    '16-1': {
        'start': {
            '1': (670, 470),
            '2': (370, 215)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (605, 475), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (590, 385), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第二回合
            {'t': 'click', 'p': (565, 500), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (515, 410), 'ec': True, 'wo': True, 'desc': "2 lower left"},

            # 第三回合
            {'t': 'click', 'p': (508, 580), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (630, 410), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第四回合
            {'t': 'click', 'p': (395, 450), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (900, 365), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第五回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (725, 450), 'wo': True, 'desc': "1 upper left & get box"},
            {'t': 'click', 'p': (445, 330), 'desc': "2 lower left"},
        ]
    },
    '16-1-box': '16-1',
    '16-1-task': '16-1',
    '16-2': {
        'start': {
            '1': (550, 385),
            '2': (520, 560)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (565, 325), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (505, 410), 'ec': True, 'wo': True, 'desc': "2 upper right"},

            # 第二回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (455, 330), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (510, 345), 'desc': "choose 2"},
            {'t': 'click', 'p': (405, 335), 'desc': "change"},
            {'t': 'click', 'p': (395, 340), 'wo': True, 'desc': "1 left"},

            # 第三回合
            {'t': 'click', 'p': (440, 445), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (845, 455), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (728, 468), 'wo': True, 'desc': "2 lower left & get box"},
            {'t': 'click', 'p': (555, 475), 'desc': "1 lower right"},
        ]
    },
    '16-2-box': '16-2',
    '16-2-task': '16-2',
    '16-3': {
        'start': {
            '1': (940, 470),
            '2': (170, 425),
            '3': (380, 240),
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (665, 415), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (550, 315), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (640, 320), 'ec': True, 'wo': True, 'desc': "3 right"},

            # 第二回合
            {'t': 'click', 'p': (720, 280), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (565, 265), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (645, 320), 'desc': "choose 2"},
            {'t': 'click', 'p': (543, 313), 'desc': "change"},
            {'t': 'click', 'p': (760, 315), 'ec': True, 'wo': True, 'desc': "3 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (440, 445), 'ec': True, 'desc': "2 lower left"},
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'exchange', 'ec': True, 'desc': "change to 3"},
            {'t': 'click', 'p': (835, 430), 'wo': True, 'desc': "3 lower right & get box"},
            {'t': 'click', 'p': (665, 410), 'desc': "choose 2"},
            {'t': 'click', 'p': (565, 405), 'desc': "change"},
            {'t': 'click', 'p': (605, 495), 'wo': True, 'desc': "1 lower left"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'exchange', 'ec': True, 'desc': "change to 3"},
            {'t': 'click', 'p': (845, 325), 'ec': True, 'desc': "3 upper left"},
            {'t': 'click', 'p': (435, 490), 'desc': "1 lower left"},
        ]
    },
    '16-3-box': '16-3',
    '16-3-task': '16-3',
}
