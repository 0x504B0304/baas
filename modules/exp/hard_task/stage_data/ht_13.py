stage_data = {
    '13-1': {
        'start': {
            '1': (730, 260),
            '2': (845, 440)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (585, 340), 'wo': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (645, 420), 'wo': True, 'desc': "2 left"},

            # 第二回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (555, 430), 'ec': True, 'desc': "2 left"},
            {'t': 'click', 'p': (560, 430), 'desc': "choose 2"},
            {'t': 'click', 'p': (457, 425), 'desc': "change"},
            {'t': 'click', 'p': (500, 515), 'wo': True, 'desc': "1 upper left"},

            # 第三回合
            {'t': 'click', 'p': (430, 475), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (840, 290), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (885, 340), 'wo': True, 'desc': "2 right & get box"},
            {'t': 'click', 'p': (400, 465), 'desc': "1 right"},
        ]
    },
    '13-1-box': '13-1',
    '13-1-task': '13-1',
    '13-2': {
        'start': {
            '1': (758, 222),
            '2': (845, 445)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (590, 340), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (650, 425), 'ec': True, 'wo': True, 'desc': "2 left"},

            # 第二回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (600, 350), 'ec': True, 'desc': "2 left"},
            {'t': 'click', 'p': (600, 350), 'desc': "choose 2"},
            {'t': 'click', 'p': (490, 345), 'desc': "change"},
            {'t': 'click', 'p': (480, 350), 'wo': True, 'desc': "1 left"},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (825, 290), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (455, 365), 'wo': True, 'desc': "1 upper left & get box"},

            # 第四回合
            {'t': 'click', 'p': (440, 450), 'desc': "1  lower left"},
        ]
    },
    '13-2-box': '13-2',
    '13-2-task': {
        'start': {
            '1': (758, 222),
            '2': (845, 445)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (590, 340), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (650, 425), 'ec': True, 'wo': True, 'desc': "2 left"},

            # 第二回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (600, 350), 'ec': True, 'desc': "2 left"},
            {'t': 'click', 'p': (600, 350), 'desc': "choose 2"},
            {'t': 'click', 'p': (490, 345), 'desc': "change"},
            {'t': 'click', 'p': (480, 350), 'wo': True, 'desc': "1 left"},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (825, 290), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (395, 445), 'desc': "1 left"},
        ]
    },
    '13-3': {
        'start': {
            '1': (785, 185),
            '2': (365, 275)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (660, 355), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (615, 370), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第二回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (675, 450), 'ec': True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (675, 445), 'desc': "choose 2"},
            {'t': 'click', 'p': (575, 445), 'desc': "change"},
            {'t': 'click', 'p': (615, 535), 'wo': True, 'desc': "1 upper left"},

            # 第三回合
            {'t': 'click', 'p': (590, 535), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (795, 380), 'ec': True, 'wo': True, 'desc': "2 lower right"},

            # 第四回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (840, 435), 'wo': True, 'desc': "2 lower right & get box"},
            {'t': 'click', 'p': (595, 560), 'desc': "1 lower right"},
        ]
    },
    '13-3-box': '13-3',
    '13-3-task': '13-3',
}
