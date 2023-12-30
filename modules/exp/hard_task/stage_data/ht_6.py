stage_data = {
    '6-1': {
        'start': {
            '1': (555, 220),
            '2': (454, 432)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (693, 333), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (569, 508), 'ec': True, "wait-over": True, "desc": "2 lower right"},

            # 第二回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (711, 455), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (777, 308), "wait-over": True, "desc": "1 right"},

            # 第三回合
            {'t': 'click', 'p': (800, 227), "desc": "1 upper right"},
            {'t': 'get-box', "wait-over": True},
            {'t': 'end-turn', 'wait-over': True},

            # 第四回合
            {'t': 'click', 'p': (774, 371), "desc": "1 lower right"},
        ]
    },
    '6-1-box': '6-1',
    '6-2': {
        'start': {
            '1': (556, 265),
            '2': (436, 441)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (534, 356), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (552, 484), 'ec': True, "wait-over": True, "desc": "2 lower right"},

            # 第二回合
            {'t': 'click', 'p': (670, 316), 'ec': True, "desc": "1 right"},
            {'t': 'click', 'p': (674, 482), "wait-over": True, "desc": "2 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (698, 382), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (696, 387), "desc": "choose 2"},
            {'t': 'click', 'p': (591, 377), "desc": "change"},
            {'t': 'click', 'p': (811, 373), "wait-over": True, "desc": "1 right"},

            # 第四回合
            {'t': 'click', 'p': (842, 301), "desc": "1 upper right"},
            {'t': 'get-box', "wait-over": True},
            {'t': 'end-turn'},
        ]
    },
    '6-2-box': '6-2',
    '6-3': {
        'start': {
            '1': (855, 515),
            '2': (569, 203)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (611, 477), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (741, 271), 'ec': True, "wait-over": True, "desc": "2 right"},

            # 第二回合
            {'t': 'click', 'p': (533, 505), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (639, 369), 'ec': True, "wait-over": True, "desc": "2 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (643, 408), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (645, 408), "desc": "choose 2"},
            {'t': 'click', 'p': (542, 405), "desc": "change"},
            {'t': 'click', 'p': (530, 412), "wait-over": True, "desc": "1 left"},

            # 第四回合
            {'t': 'exchange', 'ec': True, "desc": "change to 2"},
            {'t': 'click', 'p': (553, 485), 'ec': True, "desc": "2 left"},
            {'t': 'get-box', "wait-over": True},
            {'t': 'click', 'p': (560, 321), "desc": "1 upper left"},
        ]
    },
    '6-3-box': '6-3',
}
