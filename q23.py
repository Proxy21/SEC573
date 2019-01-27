#You will be given a list that contains two lists.  Combine the two lists and eliminate duplicates.  The answer is the SORT
#ED combined list.  [[d,b,a,c][b,d]] -> [a,b,c,d]

import local_pyWars as pyWars
game = pyWars.exercise()
y, u = game.data(23)


x = sorted(list(set(y + u)))



print (x)

game.answer(23,x)
print (game.score())
