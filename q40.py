#Read the data element and submit the number of times any instance of 
#the word 'python' (case insenstive apperas in the source"

import local_pyWars as pyWars
import re
game = pyWars.exercise()
a = game.data(40)


x = re.findall("Python", a, re.I) # re.I is re.Ignorecase you can use both
print (x)

game.answer(40,len(x))
print (game.score())
