#Given a string that contains numbers separated by
#spaces, add up the numbers and submit the sum.  "1 1 1" -> 3

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(19)
x = 0

y = y.split(' ')
print(y)
newlist = list(map(int, y))
print(y)
sum = sum(newlist)

game.answer(19,sum)
print (game.score())
