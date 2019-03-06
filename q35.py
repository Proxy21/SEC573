#The Data() method will return a tuple.  The first item in the tuple contains the absolute path of a gzip compressed file in your virtual machine.  The second item in the tuple is a line number.  Retreieve that line number from the specified file and submit it as the answer.


# THIS WILL ONLY WORK ON THE CLASS VM
import local_pyWars as pyWars
game = pyWars.exercise()
a = game.data(35)
print (a)
import gzip
