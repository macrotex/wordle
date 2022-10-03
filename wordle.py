import re

DEBUG = True
DEBUG = False

DICT = '/usr/share/dict/words'

IN_PLACE    = "...i."
IN_WORD     = "ati"
NOT_IN_WORD = "slero"

IN_PLACE    = "t...e"
IN_WORD     = "te"
NOT_IN_WORD = "slarop"

IN_PLACE    = ".ris."
IN_WORD     = ""
NOT_IN_WORD = "latehno"

def progress(msg):
    if (DEBUG):
        print(msg + "\n")

def in_place_rx(pattern):
    in_place1 = '^' + pattern.replace('.', '[a-z]') + '$'
    return re.compile(in_place1)

def in_word_rxs(pattern):
    letters = list(pattern)
    regexes = []
    for letter in letters:
        regexes.append(re.compile(f"^.*{letter}.*$"))
    return regexes

def notin_word_rxs(pattern):
    return re.compile(f"^[^{pattern}]{{5}}$")

def filter1(regexes, filepath):
    matches = None

    for rx in regexes:
        progress(f"processing regex {rx}")
        if (matches is None):
            matches = filter_on_rx(rx, filepath)
        else:
            matches = filter_on_rx_list(rx, matches)

    return matches

def filter_on_rx(regex, filepath):
    words = []
    with open(filepath) as file:
        for line in file:
            if (regex.match(line)):
                words.append(line.strip())
    return words

def filter_on_rx_list(regex, words):
    matches = []
    progress(f"processing regex {regex} on word list {words}")
    for word in words:
        progress(f"checking word {word} against regex {regex}")
        if (regex.match(word)):
            matches.append(word)

    return matches

regexes = []
regexes += [in_place_rx(IN_PLACE)]
regexes += in_word_rxs(IN_WORD)
regexes += [notin_word_rxs(NOT_IN_WORD)]

matches = filter1(regexes, DICT)
print("\n".join(matches))

