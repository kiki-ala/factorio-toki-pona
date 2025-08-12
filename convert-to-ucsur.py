#!/bin/python
#convert-to-ucsur.py

# akesi linja ni li ken ante e Lasina
#   tawa nanpa pi sitelen pona UCSUR.
# ~
# ~ this snake can change Latin letters
# ~   to sitelen pona UCSUR codepoints.

# akesi anpa ni li ken pali e ijo ante la
#   taso ni li kama tan ante mi e Factorio.
#   sona: https://wiki.factorio.com/Tutorial:Localisation
#   kin la .AHK lon: https://github.com/etbcor/nasin-nanpa/
# ~
# ~ that lowly snake might work on other things,
# ~   but it came because i was modding Factorio.
# ~   (game docs and link to reference code)

import configparser
import os
import re
from stat import S_ISDIR, S_ISREG

# poki lipu ni li toki
# ~
# ~ this directory will be read from

global SOURCE_DIR
SOURCE_DIR = "./locale"

# lipu ni li WEKA A
#   la kama sin kepeken akesi
# ~
# ~ this file will get DELETED!
# ~   and then recreated transliterated

global OUT_FILE
OUT_FILE = "./ucsur-converted/cs/tok.cfg"

# o ante ala e nimi li open sama ni.
#   ni li tan toki musi insa lipu nimi.
# ~
# ~ don't change words that start with this.
# ~   this is because of code within the file.
global IGNORE_WORDS_CONTAINING
IGNORE_WORDS_CONTAINING = "__\\d__"

global UCSUR_REPLACEMENT_TABLE
UCSUR_REPLACEMENT_TABLE = {
    "kijetesantakalu": "󱦀",
    "misikeke": "󱦇",
    "kokosila": "󱦄",
    "kepeken": "󱤙",
    "sitelen": "󱥠",
    "monsuta": "󱥽",
    "lanpan": "󱦅",
    "kalama": "󱤕",
    "kulupu": "󱤟",
    "pakala": "󱥈",
    "palisa": "󱥊 ",
    "pimeja": "󱥏",
    "sijelo": "󱥛",
    "sinpin": "󱥟",
    "soweli": "󱥢",
    "majuna": "󱦢",
    "namako": "󱥸",
    "kipisi": "󱥻",
    "jasima": "󱥿",
    "akesi": "󱤁",
    "apeja": "󱦡",
    "kiwen": "󱤛",
    "linja": "󱤩",
    "lukin": "󱤮",
    "monsi": "󱤸",
    "nanpa": "󱤽",
    "nasin": "󱤿",
    "pilin": "󱥎",
    "tenpo": "󱥫",
    "utala": "󱥱",
    "tonsi": "󱥾",
    "epiku": "󱦃",
    "alasa": "󱤃",
    "insa": "󱤏",
    "jaki": "󱤐",
    "jelo": "󱤒",
    "kala": "󱤔",
    "kama": "󱤖",
    "kasi": "󱤗",
    "kili": "󱤚",
    "kule": "󱤞",
    "kute": "󱤠",
    "lape": "󱤢",
    "laso": "󱤣",
    "lawa": "󱤤",
    "lete": "󱤦",
    "lili": "󱤨",
    "lipu": "󱤪",
    "loje": "󱤫",
    "luka": "󱤭",
    "lupa": "󱤯",
    "mama": "󱤱",
    "mani": "󱤲",
    "mije": "󱤵",
    "moku": "󱤶",
    "moli": "󱤷",
    "musi": "󱤻",
    "mute": "󱤼",
    "nasa": "󱤾",
    "nena": "󱥀",
    "nimi": "󱥂",
    "noka": "󱥃",
    "olin": "󱥅",
    "open": "󱥇",
    "pake": "󱦠",
    "pali": "󱥉",
    "pana": "󱥌",
    "pini": "󱥐",
    "pipi": "󱥑",
    "poka": "󱥒",
    "poki": "󱥓",
    "pona": "󱥔",
    "powe": "󱦣",
    "sama": "󱥖",
    "seli": "󱥗",
    "selo": "󱥘",
    "seme": "󱥙",
    "sewi": "󱥚",
    "sike": "󱥜",
    "sina": "󱥞",
    "sona": "󱥡",
    "suli": "󱥣",
    "suno": "󱥤",
    "supa": "󱥥",
    "suwi": "󱥦",
    "taso": "󱥨",
    "tawa": "󱥩",
    "telo": "󱥪",
    "toki": "󱥬",
    "tomo": "󱥭",
    "unpa": "󱥯",
    "walo": "󱥲",
    "waso": "󱥴",
    "wawa": "󱥵",
    "weka": "󱥶",
    "wile": "󱥷",
    "leko": "󱥼",
    "soko": "󱦁",
    "meso": "󱦂",
    "meli": "󱤳",
    "anpa": "󱤅",
    "ante": "󱤆",
    "awen": "󱤈",
    "esun": "󱤋",
    "ilo": "󱤎",
    "jan": "󱤑",
    "ken": "󱤘",
    "kon": "󱤝",
    "len": "󱤥",
    "lon": "󱤬",
    "mun": "󱤺",
    "ona": "󱥆",
    "pan": "󱥋",
    "sin": "󱥝",
    "tan": "󱥧",
    "uta": "󱥰",
    "wan": "󱥳",
    "kin": "󱥹",
    "oko": "󱥺",
    "ike": "󱤍",
    "ala": "󱤂",
    "ale": "󱤄",
    "anu": "󱤇",
    "ijo": "󱤌",
    "jo": "󱤓",
    "ko": "󱤜",
    "la": "󱤡",
    "li": "󱤧",
    "ma": "󱤰",
    "mi": "󱤴",
    "mu": "󱤹",
    "ni": "󱥁",
    "pi": "󱥍",
    "pu": "󱥕",
    "te": "「",
    "to": "」",
    "tu": "󱥮",
    "ku": "󱦈",
    "en": "󱤊",
    "o": "󱥄",
    "n": "󱦆",
    "a": "󱤀",
    "e": "󱤉",

    "linluwi": "󿫄",
    "kiki": "󿫃", # 󱦥
    "su": "󿬯", # 󱦦
    "isipin": "󿫀", # 
    "jami": "󿬱", # 
    "jonke": "󿭏", # 
    "kamalawala": "󿫚", # 
    "kapesi": "󿫁", # 
    "konwe": "󿭘", # 
    "kulijo": "󿫡", # 
    "melome": "󿬲", # 
    "mijomi": "󿬶", # 
    "misa": "󿫒", # 
    "mulapisu": "󿫈", # 
    "nimisin": "󿶖", # 
    "nja": "󿭠", # 
    "ojuta": "󿶃", # 
    "oke": "󿫤", # 
    "omekapo": "󿬻", # 
    "owe": "󿭥", # 
    "pakola": "󿶚", # 
    "penpo": "󿷉", # 
    "pika": "󿭪", # 
    "po": "󿫧", # 
    "puwa": "󿬼", # 
    "san": "󿫫", # 
    "soto": "󿫬", # 
    "teje": "󿫯", # 
    "sutopatikuna": "󿫻", # 
    "taki": "󿫭", # 
    "unu": "󿫊", # 
    "usawi": "󿫶", # 
    "wa": "󿫋", # 
    "wasoweli": "󿫷", # 
    "wekama": "󿬾", # 
    "wuwojiti": "󿶆", # 
    "yupekosi": "󿫼", # 
    "eliki": "󿶬", # 

    "[": "󱦐", # cartouche start
    "]": "󱦑", # cartouche end
    # "=": "󱦒", # cartouche extender (not usually necessary)

    "|": "‌\u200C", # zero width non joiner
    "&": "\u200D", # zero width joiner
    "+": "\uF1996", # scaling joiner
    "-": "\uF1995", # stacking joiner

    "(": "\uF1997", # start left-combining (normal) long glyph
    ")": "\uF1998", # end left-combining (normal) long glyph
    # "_": "\uF1999", # container extender (not usually necessary)

    "{": "\uF199A", # start right-combining (reversed) long glyph
    "}": "\uF199B", # end right-combining (reversed) long glyph

    ".": "󱦜", # sitelen pona full stop
    ":": "󱦝", # sitelen pona colon

    "\\": "゙", # dakuten
    "*": "゚", # handakuten

    "`s`s": "　", # logograph fullwidth space
    "zz": "　", # logograph fullwidth space

    # "^`<": "\u200D\u2196", # arrow NW
    # "`<^": "\u200D\u2196", # arrow NW
    # "^`>": "\u200D\u2197", # arrow NE
    # "`>^": "\u200D\u2197", # arrow NE
    # "v`>": "\u200D\u2198", # arrow SE
    # "`>v": "\u200D\u2198", # arrow SE
    # "v`<": "\u200D\u2199", # arrow SW
    # "`<v": "\u200D\u2199", # arrow SW

    # "`<": "\u200D\u2190", # arrow W
    # "^": "\u200D\u2191", # arrow N
    # "`>": "\u200D\u2192", # arrow E
    # "v": "\u200D\u2193", # arrow S

    # "1": "\uFE00", # variation selector 1
    # "2": "\uFE01", # variation selector 2
    # "3": "\uFE02", # variation selector 3
    # "4": "\uFE03", # variation selector 4
    # "5": "\uFE04", # variation selector 5
    # "6": "\uFE05", # variation selector 6
    # "7": "\uFE06", # variation selector 7
    # "8": "\uFE07", # variation selector 8
    # "9": "\uFE08", # variation selector 9
}

def lasina_localization_code_to_UCSUR(code_string):
    global UCSUR_REPLACEMENT_TABLE, IGNORE_WORDS_CONTAINING
    print("existing localisation: ", code_string)
    words = []
    for word in code_string.split(' '):
        if re.search(IGNORE_WORDS_CONTAINING, word):
            print("not transliterating", word)
            words.append(word)
        else:
            new_word = word
            if word in UCSUR_REPLACEMENT_TABLE:
                new_word = UCSUR_REPLACEMENT_TABLE[word]
            else:
                new_word_list = []
                for char in word:
                    if char in UCSUR_REPLACEMENT_TABLE.keys():
                        new_word_list.append(UCSUR_REPLACEMENT_TABLE[char])
                    else:
                        new_word_list.append(char)
                new_word = ''.join(new_word_list)
            words.append(new_word)
            print(f"{word} -> {new_word}")
    return words

def produce_transliterations_from_file(file_to_parse, accumulated_transliterations):
    config = configparser.ConfigParser(allow_unnamed_section=False)
    with open(file_to_parse, 'r', encoding="utf8") as f:
        file_string = f.read()
    file_string = file_string.replace('%', '󱥻')
    config.read_string(file_string)
    for section in config.sections():
        if section not in accumulated_transliterations.keys():
            print(f"adding section {section}")
            accumulated_transliterations[section] = {}
        for key_name in config[section]:
            print(section, key_name, ". . .")
            # this is where transliteration occurs
            code_string = config[section][key_name]
            transliterated_codepoints = lasina_localization_code_to_UCSUR(code_string)
            accumulated_transliterations[section][key_name] = ' '.join(transliterated_codepoints)

            # alternative to above for not transliterating
            # accumulated_transliterations[section][key_name] = code_string

def recurse_and_discover_content(given_path, accumulated_transliterations):
    for entry in os.listdir(given_path):
        absolute_path = os.path.join(given_path, entry)
        mode = os.lstat(absolute_path).st_mode
        if S_ISDIR(mode):
            print(f"searching {absolute_path} ...")
            recurse_and_discover_content(absolute_path, accumulated_transliterations)
        elif S_ISREG(mode) and absolute_path.endswith(".cfg"):
            print(f"- transliterating {absolute_path}")
            produce_transliterations_from_file(absolute_path, accumulated_transliterations)
        else:
            print(f"... skipping {absolute_path}")
    return accumulated_transliterations

if __name__ == "__main__":
    accum_config = configparser.ConfigParser()
    recurse_and_discover_content(SOURCE_DIR, accum_config)
    with open(OUT_FILE, 'w', encoding='utf8') as f:
        accum_config.write(f, space_around_delimiters=False)
    with open(OUT_FILE, 'r', encoding='utf8') as f:
        data = f.read().splitlines(True)
    with open(OUT_FILE, 'w', encoding='utf8') as f:
        for i, line in enumerate(data):
            if not line.strip() or line.startswith("[unnamed-section]"):
                continue
            f.writelines(data[i:])
            break
