#Data contains a dictionary.
#Submit a SORTED list of all of the values in the dictionary.

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(28)
print (y)

x = sorted(y.values())
print (x)

game.answer(28,x)
print (game.score())
