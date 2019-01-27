#Given a list of hexadecimal digits return a string
#that is made from their ASCII characters.  Ex [41 4f] -> "AO"


import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(22)
x = ""
#print (y)
for pos,val in enumerate(y):

    x += chr( int(val,16)) # int(vaule, to base16) chr(base16 to character)
    print (x)



game.answer(22,x)
print (game.score())
