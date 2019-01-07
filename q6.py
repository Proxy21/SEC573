import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(6)[::-1]


print (x)
game.answer(6,x)
print (game.score())
