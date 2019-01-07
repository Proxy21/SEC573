import local_pyWars as pyWars
import codecs
game = pyWars.exercise()

s = game.data(2)
enc = codecs.getencoder ("rot13")
x =  enc(s)[0]

game.answer(2,x)
print (game.score())
