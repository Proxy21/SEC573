#Data contains a several entries with strings and integers. 
#Each entry is separated by an exclamation mark.   
#Break each string every x characters where x is the integer after the comma.  
#For example 123456,2 becomes the list ["12", "34", "56"].  Submit a list of lists as the answer 
#[[list for first entry],[list for second entry],[list for third entry]].

import local_pyWars as pyWars
import re
game = pyWars.exercise()
#a = game.data(43)
a = []

for each in game.data(43).split("!"):
	str, num = each.split(",")
	myregex = r"." * int(num)
	thelist = re.findall(myregex, str)
	print(str, num, thelist)
	a.append(thelist)

game.answer(43,a)
print (game.score())
