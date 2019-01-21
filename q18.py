#Add the string "Pywars rocks" to the end of the list in the data element.
#Submit the new list.

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(18)
print(y)
length = len(y)
print(length)
counter = 0
x = 0


while counter < length:
    x = x + y[counter]
    print(counter)
    counter += 1
    if counter == length:
        print (x)
        game.answer(18,x)
        print (game.score())
