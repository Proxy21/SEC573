#Create a string by joining together the words "this","python","stuff","really","is","fun" by the character in .data().
#or example if data contains a hyphen (ie "-") then you submit "this-python-stuff-really-is-fun".

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(20)
print(y)
list = ["this","python","stuff","really","is","fun"]
x = ""
for pos,val in enumerate(list):
    print(pos,val)
    x += val
    if pos == 5:
        game.answer(20,x)
        print (game.score())
        exit()
    x += y
    print (x)
