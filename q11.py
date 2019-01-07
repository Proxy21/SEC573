#Leet speak it (E->3,A->4,T->7,S->5,G->6) convert only uppercase letters
#For example LeEtSpEAk->Le3t5p34k
import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(11)
x = game.data(11).replace("E","3").replace("A","4").replace("T","7").replace("S","5").replace("G","6")





print (y)
print (x)
game.answer(11,x)
print (game.score())
