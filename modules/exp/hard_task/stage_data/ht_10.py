stage_data = {
    '10-1': {
        'start': {
            '1': (757, 260),
            '2': (501, 284)
        },
        'action': [
            {'t': 'click', 'p': (642, 296), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (460, 386), 'ec': True, "desc": "2 lower left"},

            {'t': 'click', 'p': (739, 396), 'ec': True, "desc": "1 lower right"},
            {'t': 'click', 'p': (440, 473), 'ec': True, "desc": "2 lower left"},

            {'t': 'click', 'p': (645, 396), 'ec': True, "desc": "1 lower left"},
            {'t': 'end-turn', 'wait-over': True},

            {'t': 'click', 'p': (849, 394), 'ec': True, "desc": "1 right"},
            {'t': 'end-turn', 'wait-over': True},

            {'t': 'click', 'p': (901, 388), "desc": "1 right"},
        ]
    },
    '10-1-box': {
        'start': {
            '1': (757, 260),
            '2': (501, 284)
        },
        'action': [
            {'t': 'click', 'p': (701, 386), 'ec': True, "desc": "1 lower left"},
            {'t': 'click', 'p': (463, 384), 'wait-over': True, "desc": "2 lower left"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (441, 475), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (764, 398), 'wait-over': True, "desc": "1 lower right"},

            {'t': 'click', 'p': (825, 476), "desc": "1 lower right"},
            {'t': 'get-box'},
            {'t': 'end-turn', 'wait-over': True},

            {'t': 'click', 'p': (832, 342), "desc": "1 upper right"},
        ]
    },
    '10-2': {
        'start': {
            '1': (463, 260),
            '2': (637, 305)
        },
        'action': [
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (577, 472), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (583, 468), "desc": "choose 2"},
            {'t': 'click', 'p': (477, 468), "desc": "change"},
            {'t': 'click', 'p': (640, 555), 'wait-over': True, "desc": "1 lower right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (463, 425), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (743, 424), 'wait-over': True, "desc": "1 right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (469, 234), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (773, 387), 'wait-over': True, "desc": "1 right"},

            {'t': 'click', 'p': (833, 349), "desc": "1 right"},
        ]
    },
    '10-2-box': {
        'start': {
            '1': (463, 260),
            '2': (637, 305)
        },
        'action': [
            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (577, 472), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (583, 468), "desc": "choose 2"},
            {'t': 'click', 'p': (477, 468), "desc": "change"},
            {'t': 'click', 'p': (640, 555), 'wait-over': True, "desc": "1 lower right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (463, 425), 'ec': True, "desc": "2 lower left"},
            {'t': 'click', 'p': (743, 424), 'wait-over': True, "desc": "1 right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (469, 234), 'ec': True, "desc": "2 upper left"},
            {'t': 'click', 'p': (773, 387), 'wait-over': True, "desc": "1 right"},

            {'t': 'click', 'p': (773, 265), "desc": "1 upper right"},
            {'t': 'end-turn', 'wait-over': True},

            {'t': 'click', 'p': (897, 399), "desc": "1 right"},
            {'t': 'get-box'},
            {'t': 'end-turn', 'wait-over': True},

            {'t': 'click', 'p': (721, 490), "desc": "1 lower left"},
        ]
    },
    '10-3': {
        'start': {
            '1': (697, 473),
            '2': (328, 460)
        },
        'action': [
            {'t': 'click', 'p': (663, 406), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (558, 317), 'wait-over': True, "desc": "2 upper right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (672, 320), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (481, 389), "desc": "choose 2"},
            {'t': 'click', 'p': (377, 384), "desc": "change"},
            {'t': 'click', 'p': (554, 306), 'wait-over': True, "desc": "1 upper right"},

            {'t': 'click', 'p': (499, 224), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (742, 505), 'wait-over': True, "desc": "2 right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (750, 416), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (506, 293), 'wait-over': True, "desc": "1 left"},
            {'t': 'click', 'p': (387, 347), "desc": "1 left"},

        ]
    },
    '10-3-box': {
        'start': {
            '1': (697, 473),
            '2': (328, 460)
        },
        'action': [
            {'t': 'click', 'p': (663, 406), 'ec': True, "desc": "1 left"},
            {'t': 'click', 'p': (558, 317), 'wait-over': True, "desc": "2 upper right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (672, 320), 'ec': True, "desc": "2 right"},
            {'t': 'click', 'p': (481, 389), "desc": "choose 2"},
            {'t': 'click', 'p': (377, 384), "desc": "change"},
            {'t': 'click', 'p': (554, 306), 'wait-over': True, "desc": "1 upper right"},

            {'t': 'click', 'p': (499, 224), 'ec': True, "desc": "1 upper left"},
            {'t': 'click', 'p': (742, 505), 'wait-over': True, "desc": "2 right"},

            {'t': 'exchange', 'ec': True},
            {'t': 'click', 'p': (750, 416), 'ec': True, "desc": "2 upper right"},
            {'t': 'click', 'p': (567, 214), "desc": "1 upper left"},
            {'t': 'get-box', 'wait-over': True},
            {'t': 'click', 'p': (468, 393), "desc": "1 lower left"},
            {'t': 'end-turn', 'wait-over': True},

            {'t': 'click', 'p': (391, 349), "desc": "1 left"},
        ]
    },
}
