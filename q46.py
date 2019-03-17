#data has a filename and hostname of a BIND DNS log.  The awsner is a sorted list of all client ips
#in tthe log file that quried the hostname

import local_pyWars as pyWars
import re
game = pyWars.exercise()
logname, hostname = game.data(46)
#print (logname, hostname)

logfile = open("/home/student/Public/log/dnslogs/"+logname).read()

# find any ips and any hostname puts them into a tuple
b = re.findall(r"client ([\d.]{7,15})#\d{1,5}: query: (\S+) IN", logfile)

dict(b)
iplist = []

for pos,val in enumerate(b):
	if val[1] == hostname:
		iplist.append(val[0])



print (iplist)
game.answer(46,sorted(iplist))
print (game.score())
