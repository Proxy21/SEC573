#Data() contains the absolute path of a filename in your
#virtual machine.   Determine the length of the file at that path.
#Open and read the contents of the file.
#Submit the file size (length of contents) as the answer.

# THIS WILL ONLY WORK ON THE CLASS VM
import local_pyWars as pyWars
game = pyWars.exercise()
a = game.data(33)
print (a)

filecontent = open(a).read()
x = len(filecontent)
game.answer(33,x)
print (game.score())
