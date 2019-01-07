import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(5).index("SANS")


print (x)
game.answer(5,x)
print (game.score())
