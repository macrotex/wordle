# Wordle word finder

This code generates a list of Wordle words that match a partial Wordle
puzzle. This is most easily seen with an example. Here is Wordle puzzle from
September 2022:

![Wordle puzzle](wordle-example.png)


Here is the code to generate a list of possible word matches given the first two
lines of the above puzzle:
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
