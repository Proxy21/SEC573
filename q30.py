#Data contains a dictionary.  Add together the integers stored in the dictionary
#entries with the keys "python" and "rocks" and submit their sum.


import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(30)
print (y)

a = y['python'] + y['rocks']
print (a)

game.answer(30,a)
print (game.score())
