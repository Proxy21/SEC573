### swap first and last char of a string

import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(9)
def num9(x):
    return x[-1] + x[1:-1] + x[0]

x = num9(x)
print (x)
game.answer(9,x)
print (game.score())
