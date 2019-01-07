### reverse the first half of the data ex sandwich > dnaswich

import local_pyWars as pyWars
game = pyWars.exercise()

x = game.data(10)

def num10(x):
    #[:len(x)//2] is the first half of the string 0 to length div by 2
    #[::-1] reverse it in this case the first half
    #[len(x)//2:] last half empty space after : means end of string in this case
    return x[:len(x)//2][::-1] + x[len(x)//2:]

print (x)
game.answer(10,num10(x))
print (game.score())
