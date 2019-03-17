#Sentences end in a puncutation (.?!) followed by two spaces.  Data is a patagraph with multi sentences.
#submit a list of sentences.

import local_pyWars as pyWars
import re
game = pyWars.exercise()
a = game.data(41)
print (a)

x = re.findall(r".*?[?.!]  ",a)#r for raw strings,  .*? anything before non greedy(?), [set oif whateve] then two spaces
print (x)


game.answer(41, x)
print (game.score())
