#Data contains a dictionary.  Submit a SORTED list of
#all of the keys in the dictionary.


import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(27)


x = sorted(y.keys())
print (x)

game.answer(27,x)
print (game.score())
