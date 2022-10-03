import re

class Wordle():
    # Class variables
    DICT = '/usr/share/dict/words'
    ATOZ = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, green='.....', yellows=[], greys='', debug=False):
        self.green   = green
        self.yellows = yellows
        self.greys   = greys

        # This array keeps track of the possible letters in each position
        self.wordle = [Wordle.ATOZ, Wordle.ATOZ, Wordle.ATOZ, Wordle.ATOZ, Wordle.ATOZ]

        self.debug = debug

        self.process_green()
        self.process_yellows()
        self.process_greys()

    def progress(self, msg):
        if (self.debug):
            print(msg + "\n")


    def process_green(self):
        """For any in-place (GREEN) letters, set those now"""
        letters = list(self.green)
        for i in range(len(self.wordle)):
            if (letters[i] != '.'):
                self.wordle[i] = letters[i]
        self.progress(f"[process_green]: {self.wordle}")

    def process_yellows(self):
        """Remove from each position any yellow letters."""
        for in_word in self.yellows:
            letters = list(in_word)
            for i in range(len(self.wordle)):
                letter = letters[i]
                if (letter in self.wordle[i]):
                    # Remove
                    self.wordle[i] = self.wordle[i].replace(letter, "")

        self.progress(f"[process_yellows] {self.wordle}")

    def process_greys(self):
        letters = list(self.greys)
        for i in range(len(self.wordle)):
            for letter in letters:
                self.wordle[i] = self.wordle[i].replace(letter, "")

        self.progress(f"[process_greys] {self.wordle}")

    def regex_from_wordle(self):
        rx = ""
        for position in self.wordle:
            rx += "[" + position + "]"

        return re.compile(f"^{rx}$")

    def get_present_regexes(self):
        """From the self.yellows generate regexes"""
        letters_present = {}
        for in_word in self.yellows:
            letters = list(in_word)
            for letter in letters:
                if (letter != '.'):
                    letters_present[letter] = True

        regexes = []
        for letter in letters_present.keys():
            regexes.append(re.compile(f"^.*{letter}.*$"))

        return regexes

    def all_regexes(self):
        regex1          = self.regex_from_wordle()
        present_regexes = self.get_present_regexes()

        return [regex1] + present_regexes

    def filter_on_rx_dictionary(self, regex):
        words = []
        with open(Wordle.DICT) as file:
            for line in file:
                if (regex.match(line)):
                    words.append(line.strip())
        return words

    def filter_on_rx_list(self, regex, words):
        matches = []
        self.progress(f"processing regex {regex} on word list {words}")
        for word in words:
            self.progress(f"checking word {word} against regex {regex}")
            if (regex.match(word)):
                matches.append(word)

        return matches

    def filter(self, regexes):
        matches = None

        for rx in regexes:
            self.progress(f"processing regex {rx}")
            if (matches is None):
                matches = self.filter_on_rx_dictionary(rx)
            else:
                matches = self.filter_on_rx_list(rx, matches)

        return matches

    def get_matches(self):
        """This is what you want to run to get the matches."""
        all_regexes = self.all_regexes()
        return self.filter(all_regexes)


########################################################################################
########################################################################################
########################################################################################
########################################################################################

"""
#IN_PLACE    = "....."
#YELLOWS    = ["ra..n", "..a.."]
#GREYS = "stledo"

IN_PLACE    = "t...e"
YELLOWS     = ["...t."]
GREYS = "slarop"

#IN_PLACE    = "....e"
#YELLOWS    = ["d....", "..id."]
#GREYS = "stalronch"

GREEN    = "s...."
YELLOWS     = ["r..no"]
GREYS = "latehi"

GREEN     = "....."
YELLOWS     = ["s....", "r...."]
GREYS = "latehino"

GREEN     = "....."
YELLOWS     = ["..at.", ".at.."]
GREYS = "slero"

#GREEN     = "....."
#YELLOWS     = ["..a..", "ra..n"]
#GREYS = "stledo"

GREEN     = "s...."
YELLOWS     = ["...t.", ".n..t"]
GREYS = "laeou"

wordle = Wordle(green=GREEN,
                yellows=YELLOWS,
                greys=GREYS,
                debug=False,
                )

matches = wordle.get_matches()
print("\n".join(matches))
"""
