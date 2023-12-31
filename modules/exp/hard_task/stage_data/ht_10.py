stage_data = {
    '10-1': {
        'start': {
            '1': (757, 260),
            '2': (501, 284)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (642, 296), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (460, 386), 'ec': True, 'desc': "2 lower left"},

            # 第二回合
            {'t': 'click', 'p': (739, 396), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (440, 473), 'ec': True, 'desc': "2 lower left"},

            # 第三回合
            {'t': 'click', 'p': (645, 396), 'ec': True, 'desc': "1 lower left"},
            {'t': 'end-turn', 'wait-over': True},

            # 第四回合
            {'t': 'click', 'p': (849, 394), 'ec': True, 'desc': "1 right"},
            {'t': 'end-turn', 'wait-over': True},

            # 第五回合
            {'t': 'click', 'p': (901, 388), 'desc': "1 right"},
        ]
    },
    '10-1-box': {
        'start': {
            '1': (757, 260),
            '2': (501, 284)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (701, 386), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (463, 384), 'wait-over': True, 'desc': "2 lower left"},

            # 第二回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (441, 475), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (764, 398), 'wait-over': True, 'desc': "1 lower right"},

            # 第三回合
            {'t': 'click', 'p': (825, 476), 'wait-over': True, 'desc': "1 lower right & get box"},
            {'t': 'end-turn', 'wait-over': True},

            # 第四回合
            {'t': 'click', 'p': (832, 342), 'desc': "1 upper right"},
        ]
    },
    '10-1-task': '10-1-box',
    '10-2': {
        'start': {
            '1': (463, 260),
            '2': (637, 305)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (577, 472), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (583, 468), 'desc': "choose 2"},
            {'t': 'click', 'p': (477, 468), 'desc': "change"},
            {'t': 'click', 'p': (640, 555), 'wait-over': True, 'desc': "1 lower right"},

            # 第二回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (463, 425), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (743, 424), 'wait-over': True, 'desc': "1 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (469, 234), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (773, 387), 'wait-over': True, 'desc': "1 right"},

            # 第四回合
            {'t': 'click', 'p': (773, 265), 'desc': "1 upper right"},
            {'t': 'end-turn', 'wait-over': True},

            # 第五回合
            {'t': 'click', 'p': (897, 399), 'wait-over': True, 'desc': "1 right & get box"},
            {'t': 'end-turn', 'wait-over': True},

            # 第六回合
            {'t': 'click', 'p': (721, 490), 'desc': "1 lower left"},
        ]
    },
    '10-2-box': '10-2',
    '10-2-task': {
        'start': {
            '1': (463, 260),
            '2': (637, 305)
        },
        'action': [
            # 第一回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (577, 472), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (583, 468), 'desc': "choose 2"},
            {'t': 'click', 'p': (477, 468), 'desc': "change"},
            {'t': 'click', 'p': (640, 555), 'wait-over': True, 'desc': "1 lower right"},

            # 第二回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (463, 425), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (743, 424), 'wait-over': True, 'desc': "1 right"},

            # 第三回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (469, 234), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (773, 387), 'wait-over': True, 'desc': "1 right"},

            # 第四回合
            {'t': 'click', 'p': (833, 349), 'desc': "1 right"},
        ]
    },
    '10-3': {
        'start': {
            '1': (697, 473),
            '2': (328, 460)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (663, 406), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (558, 317), 'wait-over': True, 'desc': "2 upper right"},

            # 第二回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (672, 320), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (481, 389), 'desc': "choose 2"},
            {'t': 'click', 'p': (377, 384), 'desc': "change"},
            {'t': 'click', 'p': (554, 306), 'wait-over': True, 'desc': "1 upper right"},

            # 第三回合
            {'t': 'click', 'p': (499, 224), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (742, 505), 'wait-over': True, 'desc': "2 right"},

            # 第四回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (750, 416), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (567, 214), 'wait-over': True, 'desc': "1 upper left & get box"},
            {'t': 'click', 'p': (468, 393), 'desc': "1 lower left"},
            {'t': 'end-turn', 'wait-over': True},

            # 第五回合
            {'t': 'click', 'p': (391, 349), 'desc': "1 left"},
        ]
    },
    '10-3-box': '10-3',
    '10-3-task': {
        'start': {
            '1': (697, 473),
            '2': (328, 460)
        },
        'action': [
            # 第一回合
            {'t': 'click', 'p': (663, 406), 'ec': True, 'desc': "1 left"},
            {'t': 'click', 'p': (558, 317), 'wait-over': True, 'desc': "2 upper right"},

            # 第二回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (672, 320), 'ec': True, 'desc': "2 right"},
            {'t': 'click', 'p': (481, 389), 'desc': "choose 2"},
            {'t': 'click', 'p': (377, 384), 'desc': "change"},
            {'t': 'click', 'p': (554, 306), 'wait-over': True, 'desc': "1 upper right"},

            # 第三回合
            {'t': 'click', 'p': (499, 224), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (742, 505), 'wait-over': True, 'desc': "2 right"},

            # 第四回合
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (750, 416), 'ec': True, 'desc': "2 upper right"},
            {'t': 'click', 'p': (506, 293), 'wait-over': True, 'desc': "1 left"},
            {'t': 'click', 'p': (387, 347), 'desc': "1 left"},

        ]
    },
}
