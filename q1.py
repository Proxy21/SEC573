import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(1)
x += 5

game.answer(1,x)
print (game.score())
