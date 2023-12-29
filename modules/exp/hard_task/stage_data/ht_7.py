stage_data = {
    '7-1': {
        'start': {
            '1': (825, 386),
            '2': (777, 560)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (652, 233), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (570, 490), 'ec': True, "wait-over": True, "desc": "2 left"},

            # 第二回合
            {'t': 'click', 'p': (550, 300), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (496, 507), "desc": "1 lower left"},
            {'t': 'move', 'ec': True, "wait-over": True, "desc": "teleport"},

            # 第三回合
            {'t': 'click', 'p': (666, 356), "desc": "choose 2"},
            {'t': 'click', 'p': (565, 350), "desc": "change"},
            {'t': 'click', 'p': (667, 356), "desc": "click teleport"},
            {'t': 'move', "wait-over": True, "desc": "teleport"},
            {'t': 'click', 'p': (529, 369), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (529, 271), "wait-over": True, "desc": "2 left"},
            {'t': 'get-box'},

            # 第四回合
            {'t': 'click', 'p': (488, 382), "desc": "1 upper left"},
        ]
    },
    '7-1-box': '7-1',
}
