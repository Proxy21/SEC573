#Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.  The value for each of those entries is another dictionary.  That dictionary contains Operating System classes as the key and its percentage of use in the target organization as the value.  You have an exploit that will work against XP, NT and VISTA.  What month had the most vulnerable targets?  IE Add up the percentage for XP, NT and Vista.  Submit the month (1,2,3,4,5,6,7,8,9,10,11 #or 12) that has the highest percentage. If two months have the same percentage submit the most recent.

import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(32)
a = 0
b = "date"
#print (y)
master = {}

for pos,val in enumerate(y):
    master[val] = (float(y[val]["WinXP"]) + float(y[val]["NT*"]) + float(y[val]["Vista"]))

for pos,val in enumerate(master):

    if master[val] > a:
        a = master[val]
        b = val
b = b[:2]
c, d = b
b = c + d
if d == "-":
    b = c

print (c)

game.answer(32,b)
print (game.score())
print(a, b)
print(master)
