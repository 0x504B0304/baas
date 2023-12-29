stage_data = {
    '6-1': '6-1-box',
    '6-1-box': {
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
            {'t': 'get-box'},
            {'t': 'end-turn', 'wait-over': True},

            # 第四回合
            {'t': 'click', 'p': (774, 371), "desc": "1 lower right"},
        ]
    },
}
