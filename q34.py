#The data() method returns an abosolute path to a directory on your file system.
# Submit a sorted list of the filenames in that directory.

# THIS WILL ONLY WORK ON THE CLASS VM
import local_pyWars as pyWars
import os
game = pyWars.exercise()
a = game.data(34)
print (a)
import os
x = sorted(os.listdir(a))

game.answer(34,x)
print (game.score())
