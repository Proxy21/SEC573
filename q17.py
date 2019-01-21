#Add the string "Pywars rocks" to the end of the list in the data element.
#Submit the new list.

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(17)
print(y)
wars = 'Pywars rocks'

y.append(wars)
print (y)

game.answer(17,y)
print (game.score())
