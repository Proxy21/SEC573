### return 2 5 9th charachters
import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(8)[1] + game.data(8)[4] + game.data(8)[8]


print (x)
game.answer(8,x)
print (game.score())
