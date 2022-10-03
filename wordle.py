import re

DEBUG = True
#DEBUG = False


class Wordle():
    # Class variables
    DICT = '/usr/share/dict/words'
    ATOZ = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, in_place='.....', in_words=[], letters_not_in_word='', debug=False):
        self.in_place            = in_place
        self.in_words            = in_words
        self.letters_not_in_word = letters_not_in_word

        # This array keeps track of the possible letters in each position
        self.wordle = [Wordle.ATOZ, Wordle.ATOZ, Wordle.ATOZ, Wordle.ATOZ, Wordle.ATOZ]

        self.debug = debug

        self.process_green()
        self.process_yellow()
        self.process_grey()

    def progress(self, msg):
        if (self.debug):
            print(msg + "\n")


    def process_green(self):
        """For any in-place (GREEN) letters, set those now"""
        letters = list(self.in_place)
        for i in range(len(self.wordle)):
            if (letters[i] != '.'):
                self.wordle[i] = letters[i]
        self.progress(f"in_place: {self.wordle}")

    def process_yellow(self):
        """Remove from each position any yellow letters."""
        for in_word in self.in_words:
            letters = list(in_word)
            for i in range(len(self.wordle)):
                letter = letters[i]
                if (letter in self.wordle[i]):
                    # Remove
                    self.wordle[i] = self.wordle[i].replace(letter, "")

        self.progress(f"[remove_yellow] {self.wordle}")

    def process_grey(self):
        letters = list(self.letters_not_in_word)
        for i in range(len(self.wordle)):
            for letter in letters:
                self.wordle[i] = self.wordle[i].replace(letter, "")

        self.progress(f"[remove_grey] {self.wordle}")

    def regex_from_wordle(self):
        rx = ""
        for position in self.wordle:
            rx += "[" + position + "]"

        return re.compile(f"^{rx}$")

    def get_present_regexes(self):
        """From the self.in_words generate regexes"""
        letters_present = {}
        for in_word in self.in_words:
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
        all_regexes = self.all_regexes()
        return self.filter(all_regexes)


########################################################################################
########################################################################################
########################################################################################
########################################################################################

IN_PLACE    = "...i."
IN_WORD     = "ati"
NOT_IN_WORD = "slero"


#IN_PLACE    = "....."
#IN_WORDS    = ["ra..n", "..a.."]
#NOT_IN_WORD = "stledo"

IN_PLACE    = "t...e"
IN_WORDS     = ["...t."]
NOT_IN_WORD = "slarop"

#IN_PLACE    = "....e"
#IN_WORDS    = ["d....", "..id."]
#NOT_IN_WORD = "stalronch"

IN_PLACE    = "s...."
IN_WORDS     = ["r..no"]
NOT_IN_WORD = "latehi"

IN_PLACE     = "....."
IN_WORDS     = ["s....", "r...."]
NOT_IN_WORD = "latehino"

IN_PLACE     = "....."
IN_WORDS     = ["..at.", ".at.."]
NOT_IN_WORD = "slero"

IN_PLACE     = "....."
IN_WORDS     = ["..a..", "ra..n"]
NOT_IN_WORD = "stledo"

wordle = Wordle(in_place=IN_PLACE,
                in_words=IN_WORDS,
                letters_not_in_word=NOT_IN_WORD,
                debug=False,
                )

matches = wordle.get_matches()
print("\n".join(matches))
