#extract the SSNs from data.  SSN is either 9 digits or 'XXX-XX-XXXX'(space or dash). 
#submit the list in order they appear.  All ssn should be in xxx-xx-xxxx format.
 
import local_pyWars as pyWars
import re
game = pyWars.exercise()
a = game.data(42)


#three digits then space or dash. ? means optional.  Then you get a list then slice the strings so all at like this xxx-xx-xxxx
#x = re.findall(r"\d{3}[ -]?\d{2}[ -]?\d{4}",a)

#same but with group so it returns a tuple with each set of nums you can then just join with a -
#map to join the list but it creates an object so then we put list outside
x = list(map("-".join, re.findall(r"(\d{3})[ -]?(\d{2})[ -]?(\d{4})",a)))

print (x)
game.answer(42,x)
print (game.score())
