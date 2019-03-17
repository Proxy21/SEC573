#The data() method will returen a string.  Find all text files beneath /home/student/public/log that contain that string
#The Answer is a sorted list of all the ab paths to files that contain the string.  Do not uncompress gzips
#
#


# THIS WILL ONLY WORK ON THE CLASS VM
import local_pyWars as pyWars
import os
game = pyWars.exercise()
a = game.data(36)
print (a)

answer = []
for cwd,lod,lof in os.walk("/home/student/Public/log/"): #cwd Current workingdir, list of dir, list of files.
	for eachfile in lof:
		filecontent = open(cwd +"/"+ eachfile,"rb").read() #"/" only for linux use os.path.join for both windows and linux "rb" to read in bytes so you can also search the gzip files
		if a.encode() in filecontent:
			answer.append(cwd +"/"+ eachfile)
		
		

game.answer(36,sorted(answer))
print (game.score())
