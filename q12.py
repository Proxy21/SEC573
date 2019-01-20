#Read the list from data and return the 3rd element
import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(12)
x = y[2]




print (y)
print (x)
game.answer(12,x)
print (game.score())
