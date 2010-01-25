IMAGE_NAMES = 'data/mapNames.png'
IMAGE_MAP = 'data/in.png'
IMAGE_ARMY = 'data/army.png'
IMAGE_FLEET = 'data/fleet.png'
INDEX_COLOR=0
INDEX_TYPEMASK=1
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
LAND = 0x1 << 1
SEA = 0x1 << 2

def is_land(loc):
    return DIP[loc][INDEX_TYPEMASK] & LAND > 0

def is_coast_or_sea(loc):
    return DIP[loc][INDEX_TYPEMASK] & SEA > 0

DIP = {
    'spa_nc': ((250,0,0), LAND | SEA, (138,651)),
    'spa_sc': ((250,0,0), LAND | SEA, (188,836)),
    'bul_nc': ((90,0,0), LAND | SEA, (788,746)),
    'bul_sc': ((90,0,0), LAND | SEA, (740,818)),
    'stp_nc': ((0,200,0), LAND | SEA, (922,88)),
    'stp_sc': ((0,200,0), LAND | SEA, (754,324)),
    'spa': ((250,0,0), LAND, (190,754)),
    'por': ((0,0,50), LAND | SEA, (82,746)),
    'naf': ((0,0,60), LAND | SEA, (192,931)),
    'tun': ((0,0,70), LAND | SEA, (412,936)),
    'gre': ((0,0,130), LAND | SEA, (679,873)),
    'bul': ((90,0,0), LAND, (729,762)),
    'alb': ((80,0,0), LAND | SEA, (635,812)),
    'ser': ((70,0,0), LAND, (650,773)),
    'rum': ((100,0,0), LAND | SEA, (766,706)),
    'con': ((110,0,0), LAND | SEA, (802,832)),
    'smy': ((0,0,110), LAND | SEA, (833,891)),
    'ank': ((0,0,100), LAND | SEA, (952,817)),
    'arm': ((0,0,90), LAND | SEA, (1122,828)),
    'syr': ((0,0,80), LAND | SEA, (1133,943)),
    'sev': ((0,180,0), LAND | SEA, (897,586)),
    'ruh': ((0,60,0), LAND, (439,548)),
    'ven': ((120,0,0), LAND | SEA, (487,707)),
    'tus': ((160,0,0), LAND | SEA, (470,748)),
    'rom': ((150,0,0), LAND | SEA, (510,802)),
    'nap': ((140,0,0), LAND | SEA, (552,846)),
    'apu': ((130,0,0), LAND | SEA, (578,821)),
    'ukr': ((0,170,0), LAND, (765,565)),
    'lvn': ((0,160,0), LAND | SEA, (709,432)),
    'mos': ((0,190,0), LAND, (884,426)),
    'stp': ((0,200,0), LAND | SEA, (966,202)),
    'fin': ((0,150,0), LAND | SEA, (695,226)),
    'swe': ((0,140,0), LAND | SEA, (577,257)),
    'nor': ((0,130,0), LAND | SEA, (510,266)),
    'den': ((0,120,0), LAND | SEA, (495,409)),
    'war': ((0,210,0), LAND, (654,541)),
    'sil': ((0,80,0), LAND, (579,537)),
    'mun': ((0,70,0), LAND, (478,587)),
    'trl': ((50,0,0), LAND, (530,634)),
    'tri': ((60,0,0), LAND | SEA, (571,707)),
    'pie': ((170,0,0), LAND | SEA, (428,687)),
    'mar': ((180,0,0), LAND | SEA, (363,692)),
    'bur': ((200,0,0), LAND, (388,625)),
    'gas': ((190,0,0), LAND | SEA, (297,667)),
    'par': ((210,0,0), LAND, (334,606)),
    'bre': ((220,0,0), LAND | SEA, (281,574)),
    'pic': ((230,0,0), LAND | SEA, (350,553)),
    'bud': ((0,230,0), LAND, (660,664)),
    'vie': ((0,240,0), LAND, (588,630)),
    'boh': ((0,250,0), LAND, (553,581)),
    'gal': ((0,220,0), LAND, (680,593)),
    'pru': ((0,90,0), LAND | SEA, (602,485)),
    'ber': ((0,100,0), LAND | SEA, (541,472)),
    'kie': ((0,110,0), LAND | SEA, (477,497)),
    'hol': ((0,50,0), LAND | SEA, (422,489)),
    'bel': ((240,0,0), LAND | SEA, (392,525)),
    'edi': ((0,0,180), LAND | SEA, (328,335)),
    'yor': ((0,0,160), LAND | SEA, (340,427)),
    'lvp': ((0,0,170), LAND | SEA, (312,400)),
    'lon': ((0,0,140), LAND | SEA, (352,481)),
    'wal': ((0,0,150), LAND | SEA, (289,463)),
    'cly': ((0,0,190), LAND | SEA, (297,331)),
    # begin oceans
    'iri': ((0,0,170), SEA, (200,477)),
    'bla': (COLOR_OCEAN, SEA, (917,733)),
    'nao': (COLOR_OCEAN, SEA, (104,217)),
    'eas': (COLOR_OCEAN, SEA, (848,961)),
    'aeg': (COLOR_OCEAN, SEA, (749,903)),
    'ion': (COLOR_OCEAN, SEA, (589,942)),
    'tyr': (COLOR_OCEAN, SEA, (465,836)),
    'adr': (COLOR_OCEAN, SEA, (553,763)),
    'lyo': (COLOR_OCEAN, SEA, (360,765)),
    'wes': (COLOR_OCEAN, SEA, (302,843)),
    'mao': (COLOR_OCEAN, SEA, (78,577)),
    'nth': (COLOR_OCEAN, SEA, (403,383)),
    'nwg': (COLOR_OCEAN, SEA, (427,105)),
    'ska': (COLOR_OCEAN, SEA, (501,361)),
    'hel': (COLOR_OCEAN, SEA, (447,442)),
    'bal': (COLOR_OCEAN, SEA, (610,428)),
    'bot': (COLOR_OCEAN, SEA, (647,321)),
    'bar': (COLOR_OCEAN, SEA, (838,36)),
}

UNALIGNED = [ 'spa', 'por', 'naf', 'tun', 'hol', 'bel', 'nor', 'swe', 'den', 'rum', 'bul', 'ser', 'alb', 'gre' ]
DEFAULT_ENGLAND = [ 'cly', 'yor', 'lon', 'wal', 'lvp', 'edi' ]
DEFAULT_FRANCE = [ 'bre', 'par', 'bur', 'pic', 'gas', 'mar' ]
DEFAULT_GERMANY = [ 'kie', 'ber', 'pru', 'sil', 'mun', 'ruh' ]
DEFAULT_AUSTRIA = [ 'boh', 'vie', 'tri', 'bud', 'gal', 'trl' ]
DEFAULT_ITALY = [ 'pie', 'ven', 'tus', 'rom', 'nap', 'apu' ]
DEFAULT_TURKEY = [ 'con', 'ank', 'smy', 'syr', 'arm' ]
DEFAULT_RUSSIA = [ 'fin', 'stp', 'mos', 'sev', 'ukr', 'war', 'lvn' ]
