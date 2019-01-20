#Build a list of numbers starting at 1 and up to but
#not including the number in data().
import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(13)
#x = y[2]
list = []
counter = 0

while counter < y:
    counter += 1
    list.extend([counter])
    if counter == y-1:
        print (list)
        game.answer(13,list)




print (y)

print (game.score())
