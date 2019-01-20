#Split the data element based on the comma (",")
#delimiter and return the 10th element

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(15)
y = y.replace(',', '')
x = list(y)
print (x)

game.answer(15,x[9])
print (game.score())
