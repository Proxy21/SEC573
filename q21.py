#The answer is the list of numbers between 1 and 1000 that are evenly divisible by the number provided.
#2->[2,4,6,8..] 4->[4,8,16..]

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(21)
print (y)
list = []

for each in range(1, 1001):
    if each%y == 0:
        list.append(each)

game.answer(21,list)
print (game.score())
