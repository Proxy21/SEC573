#count the number of items in the list in data().
#The answer is the number of items in the list.

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(14)
print (y)

x = len(y)
print (x)
game.answer(14,x)
print (game.score())
