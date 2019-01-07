import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(4).upper()

print (x)
game.answer(4,x)
print (game.score())
