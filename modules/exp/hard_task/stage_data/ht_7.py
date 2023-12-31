stage_data = {
    '7-1': {
        'start': {
            '1': (825, 386),
            '2': (777, 560)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (652, 233), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (570, 490), 'ec': True, 'wo': True, 'desc': "2 left"},

            # 第二回合
            {'t': 'click', 'p': (550, 300), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (496, 507), 'desc': "1 lower left"},
            {'t': 'move', 'ec': True, 'wo': True, 'desc': "teleport"},

            # 第三回合
            {'t': 'click', 'p': (666, 356), 'desc': "choose 2"},
            {'t': 'click', 'p': (565, 350), 'desc': "change"},
            {'t': 'click', 'p': (667, 356), 'desc': "click teleport"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (529, 369), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (529, 271), 'wo': True, 'desc': "2 left & get box"},

            # 第四回合
            {'t': 'click', 'p': (488, 382), 'desc': "1 upper left"},
        ]
    },
    '7-1-box': '7-1',
    '7-1-task': {
        'start': {
            '1': (825, 386),
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (656, 383), 'desc': "1 left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},

            # 第二回合
            {'t': 'click', 'p': (536, 352), 'wo': True, 'desc': "1 upper left"},

            # 第三回合
            {'t': 'click', 'p': (478, 278), 'desc': "1 upper left"},

        ]
    },
    '7-2': {
        'start': {
            '1': (470, 225),
            '2': (656, 297)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (580, 470), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (762, 388), 'ec': True, 'wo': True, 'desc': "2 left"},

            # 第二回合
            {'t': 'click', 'p': (521, 560), 'desc': "1 lower left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},
            {'t': 'click', 'p': (762, 366), 'wo': True, 'desc': "2 lower right & get box"},

            # 第三回合
            {'t': 'click', 'p': (736, 407), 'desc': "1 upper right", 'wo': True},
            {'t': 'end-turn'},
        ]
    },
    '7-2-box': '7-2',
    '7-2-task': {
        'start': {
            '1': (470, 225),
            '2': (656, 297)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (582, 484), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (577, 471), 'desc': "choose 2"},
            {'t': 'click', 'p': (477, 468), 'desc': "change"},
            {'t': 'click', 'p': (520, 555), 'desc': "1 lower left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},

            # 第二回合
            {'t': 'click', 'p': (717, 374), 'ec': True, 'desc': "1 upper left"},
            {'t': 'end-turn'},
        ]
    },
    '7-3': {
        'start': {
            '1': (943, 470),
            '2': (187, 263)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (660, 432), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (642, 350), 'ec': True, 'wo': True, 'desc': "2 right"},

            # 第二回合
            {'t': 'click', 'p': (669, 385), 'desc': "1 left"},
            {'t': 'move', 'wo': True, 'desc': "teleport"},

            {'t': 'click', 'p': (597, 388), 'desc': "2 lower right"},
            {'t': 'move', 'wo': True, 'desc': "teleport", "after": 8},

            # 第三回合
            {'t': 'exchange', 'ec': True, 'desc': "change to 2"},
            {'t': 'click', 'p': (450, 497), 'wo': True, 'desc': "2 left & get box"},

            {'t': 'click', 'p': (842, 290), 'desc': "1 left"},
        ]
    },
    '7-3-box': '7-3',
    '7-3-task': '7-3',
}
