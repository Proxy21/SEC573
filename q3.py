import local_pyWars as pyWars
import base64
game = pyWars.exercise()

y = game.data(3)
x = base64.b64decode(y)

game.answer(3,x)
print (game.score())
