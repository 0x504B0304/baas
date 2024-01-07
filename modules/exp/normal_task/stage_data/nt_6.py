stage_data = {
    '6-1': {
        'start': {
            '1': (494, 269),
            '2': (467, 548)
        },
        'action': [
            {'t': 'click', 'p': (682, 348), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (697, 490), 'wo': True, 'ec': True, 'desc': "2 right"},

            {'t': 'click', 'p': (781, 326), 'ec': True, 'desc': "1 right"},
            {'t': 'end-turn', 'ec': True, 'desc': 'round over', 'wo': True},

            {'t': 'click', 'p': (844, 328), 'ec': True, 'desc': "1 right"},
            {'t': 'end-turn'},

        ]
    },
    '6-2': {
        'start': {
            '1': (460, 556),
            '2': (499, 216)
        },
        'action': [
            {'t': 'click', 'p': (680, 418), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (695, 280), 'wo': True, 'ec': True, 'desc': "2 right"},

            {'t': 'click', 'p': (815, 447), 'ec': True, 'desc': "1 right"},
            {'t': 'click', 'p': (775, 267), 'wo': True, 'ec': True, 'desc': "2 right"},

            {'t': 'click', 'p': (754, 413), 'ec': True, 'desc': "1 right"},
            {'t': 'end-turn'},

        ]
    },
    '6-3': {
        'start': {
            '1': (520, 560),
            '2': (466, 146)
        },
        'action': [
            {'t': 'click', 'p': (721, 420), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (647, 362), 'wo': True, 'ec': True, 'desc': "2 lower right"},

            {'t': 'click', 'p': (761, 408), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (700, 328), 'wo': True, 'ec': True, 'desc': "2 right"},

            {'t': 'click', 'p': (661, 386), 'desc': "1 right"},
        ]
    },
    '6-4': {
        'start': {
            '1': (403, 347),
            '2': (679, 285)
        },
        'action': [
            {'t': 'exchange', 'ec': True, 'desc': 'change to 2'},
            {'t': 'click', 'p': (629, 447), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (629, 447), 'desc': "choose 2"},
            {'t': 'click', 'p': (529, 447), 'desc': "change 1 2"},
            {'t': 'click', 'p': (692, 535), 'wo': True, 'desc': "1 lower right"},

            {'t': 'click', 'p': (625, 432), 'ec': True, 'desc': "1 lower right"},
            {'t': 'end-turn', 'ec': True, 'desc': 'round over', 'wo': True},

            {'t': 'click', 'p': (851, 484), 'ec': True, 'desc': "1 right"},
            {'t': 'end-turn'},
        ]
    },
    '6-5': {
        'start': {
            '1': (818, 261),
            '2': (583, 225)
        },
        'action': [
            {'t': 'click', 'p': (715, 429), "ec": True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (535, 348), 'wo': True, "ec": True, 'desc': "2 lower left"},

            {'t': 'exchange', 'ec': True, 'desc': 'change to 2'},
            {'t': 'click', 'p': (653, 352), "ec": True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (713, 446), 'wo': True, 'desc': "1 lower left"},

            {'t': 'click', 'p': (845, 461), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (530, 280), 'wo': True, 'ec': True, 'desc': "2 left"},

            {'t': 'click', 'p': (877, 410), 'desc': "1 right"},
        ]
    },
}
