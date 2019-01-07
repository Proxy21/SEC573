import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(7) + game.data(7)[::-1] + game.data(7)


print (x)
game.answer(7,x)
print (game.score())
