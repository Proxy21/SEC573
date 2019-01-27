#Data contains a dictionary.  Submit a SORTED list of tuples.
#There should be one tuple for each entry in the dictionary.
#Each tuple should contain a key and its associated value from the dictionary.

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(29)
print (y)


x = sorted(y.items())
print (x)

game.answer(29,x)
print (game.score())
