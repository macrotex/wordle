# Wordle word finder

This code generates a list of Wordle words that match a partial Wordle
puzzle. This is most easily seen with an example. Here is Wordle puzzle from
September 2022:

![Wordle puzzle](wordle-example.png)

Here is the code to generate a list of possible word matches given the three lines
of the above puzzle:
```
from wordle import Wordle

GREEN   = "..i.."
YELLOWS = ["s....", "r...."]
GREYS   = "latehnopm"

wordle = Wordle(green=GREEN,
                yellows=YELLOWS,
                greys=GREYS,
                )

matches = wordle.get_matches()
print("\n".join(matches))
```

The output of running the above code:
```
brigs
brisk
cribs
frisk
grids
```

That is, the solution of the above puzzle must be one of the above words. (The
actual solution for that particular puzzle was `brisk`.)

DISCLAIMER: The default word list used is `/usr/share/dict/words` which
almost certainly does _not_ match the official Wordle word list. To use a
_different_ word list specify the `dict` parameter:

```
from wordle import Wordle

GREEN   = "..i.."
YELLOWS = ["s....", "r...."]
GREYS   = "latehnopm"
DICT    = '/usr/share/some/other/wordlist'

wordle = Wordle(green=GREEN,
                yellows=YELLOWS,
                greys=GREYS,
                dict=DICT,
                )

matches = wordle.get_matches()
print("\n".join(matches))
```
