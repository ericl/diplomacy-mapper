IMAGE_NAMES = 'data/mapNames.png'
IMAGE_MAP = 'data/in.png'
IMAGE_ARMY = 'data/army.png'
IMAGE_FLEET = 'data/fleet.png'
INDEX_COLOR=0
INDEX_OCEAN=1
INDEX_COORD=2

COLOR_OCEAN = (197,223,234)
COLOR_NEUTRAL = (226,198,158)
COLOR_ENGLAND = (239,196,228)
COLOR_GERMANY = (160,138,117)
COLOR_AUSTRIA = (196,143,133)
COLOR_RUSSIA = (168,126,159)
COLOR_TURKEY = (234,234,175)
COLOR_FRANCE = (121,175,198)
COLOR_ITALY = (164,196,153)

DIP = {
    'spa_nc': ((250,0,0), False, (138,651)),
    'spa_sc': ((250,0,0), False, (188,836)),
    'bul_nc': ((90,0,0), False, (788,746)),
    'bul_sc': ((90,0,0), False, (740,818)),
    'stp_nc': ((0,200,0), False, (922,88)),
    'stp_sc': ((0,200,0), False, (754,324)),
    'spa': ((250,0,0), False, (190,754)),
    'por': ((0,0,50), False, (82,746)),
    'naf': ((0,0,60), False, (192,931)),
    'tun': ((0,0,70), False, (412,936)),
    'gre': ((0,0,130), False, (679,873)),
    'bul': ((90,0,0), False, (729,762)),
    'alb': ((80,0,0), False, (635,812)),
    'ser': ((70,0,0), False, (650,763)),
    'rum': ((100,0,0), False, (766,706)),
    'con': ((110,0,0), False, (802,832)),
    'smy': ((0,0,110), False, (833,891)),
    'ank': ((0,0,100), False, (952,817)),
    'arm': ((0,0,90), False, (1122,828)),
    'syr': ((0,0,80), False, (1133,943)),
    'sev': ((0,180,0), False, (897,586)),
    'ruh': ((0,60,0), False, (439,548)),
    'ven': ((120,0,0), False, (487,707)),
    'tus': ((160,0,0), False, (470,748)),
    'rom': ((150,0,0), False, (510,802)),
    'nap': ((140,0,0), False, (552,846)),
    'apu': ((130,0,0), False, (578,821)),
    'ukr': ((0,170,0), False, (765,565)),
    'lvn': ((0,160,0), False, (709,432)),
    'mos': ((0,190,0), False, (884,426)),
    'stp': ((0,200,0), False, (966,202)),
    'fin': ((0,150,0), False, (695,226)),
    'swe': ((0,140,0), False, (577,257)),
    'nwy': ((0,130,0), False, (510,266)),
    'den': ((0,120,0), False, (495,409)),
    'war': ((0,210,0), False, (654,541)),
    'sil': ((0,80,0), False, (579,537)),
    'mun': ((0,70,0), False, (478,587)),
    'trl': ((50,0,0), False, (530,634)),
    'tri': ((60,0,0), False, (571,707)),
    'pie': ((170,0,0), False, (428,687)),
    'mar': ((180,0,0), False, (363,692)),
    'bur': ((200,0,0), False, (388,625)),
    'gas': ((190,0,0), False, (297,667)),
    'par': ((210,0,0), False, (334,606)),
    'bre': ((220,0,0), False, (281,574)),
    'pic': ((230,0,0), False, (350,553)),
    'bud': ((0,230,0), False, (660,664)),
    'vie': ((0,240,0), False, (588,630)),
    'boh': ((0,250,0), False, (553,581)),
    'gal': ((0,220,0), False, (680,593)),
    'pru': ((0,90,0), False, (602,485)),
    'ber': ((0,100,0), False, (541,472)),
    'kie': ((0,110,0), False, (477,497)),
    'hol': ((0,50,0), False, (422,489)),
    'bel': ((240,0,0), False, (392,525)),
    'edi': ((0,0,180), False, (328,335)),
    'yor': ((0,0,160), False, (340,427)),
    'lvp': ((0,0,170), False, (312,400)),
    'lon': ((0,0,140), False, (352,481)),
    'wal': ((0,0,150), False, (289,463)),
    'cly': ((0,0,190), False, (297,331)),
    # begin oceans
    'iri': ((0,0,170), True, (200,477)),
    'bla': (COLOR_OCEAN, True, (917,733)),
    'nao': (COLOR_OCEAN, True, (104,217)),
    'eas': (COLOR_OCEAN, True, (848,961)),
    'aeg': (COLOR_OCEAN, True, (749,903)),
    'ion': (COLOR_OCEAN, True, (589,942)),
    'tyr': (COLOR_OCEAN, True, (465,836)),
    'adr': (COLOR_OCEAN, True, (553,763)),
    'lyo': (COLOR_OCEAN, True, (360,765)),
    'wes': (COLOR_OCEAN, True, (302,843)),
    'mao': (COLOR_OCEAN, True, (78,577)),
    'nth': (COLOR_OCEAN, True, (403,383)),
    'nor': (COLOR_OCEAN, True, (427,105)),
    'ska': (COLOR_OCEAN, True, (501,361)),
    'hel': (COLOR_OCEAN, True, (447,442)),
    'bal': (COLOR_OCEAN, True, (610,428)),
    'bot': (COLOR_OCEAN, True, (647,321)),
    'bar': (COLOR_OCEAN, True, (838,36)),
}

UNALIGNED = [ 'spa', 'por', 'naf', 'tun', 'hol', 'bel', 'nwy', 'swe', 'den', 'rum', 'bul', 'ser', 'alb', 'gre' ]
DEFAULT_ENGLAND = [ 'iri', 'cly', 'yor', 'lon', 'wal', 'lvp', 'edi' ]
DEFAULT_FRANCE = [ 'bre', 'par', 'bur', 'pic', 'gas', 'mar' ]
DEFAULT_GERMANY = [ 'kie', 'ber', 'pru', 'sil', 'mun', 'ruh' ]
DEFAULT_AUSTRIA = [ 'boh', 'vie', 'tri', 'bud', 'gal', 'trl' ]
DEFAULT_ITALY = [ 'pie', 'ven', 'tus', 'rom', 'nap', 'apu' ]
DEFAULT_TURKEY = [ 'con', 'ank', 'smy', 'syr', 'arm' ]
DEFAULT_RUSSIA = [ 'fin', 'stp', 'mos', 'sev', 'ukr', 'war', 'lvn' ]
