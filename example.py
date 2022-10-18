from wordle import Wordle

GREEN   = ".ris."
YELLOWS = ['s....', 'r....']
GREYS   = "latehnopm"

wordle = Wordle(green=GREEN,
                yellows=YELLOWS,
                greys=GREYS,
                )

matches = wordle.get_matches()
print("\n".join(matches))
