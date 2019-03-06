#testing opening files and stuff#

#filehandle = open("complete file path", "mode")
#or
#with open("filepath",mode) as filehandle:
    #code block toprocess file
#modes: r=read,w=write,a=append,rt=read and interpret unicode(default)
#rb =read binary and do not interpret
filehandle = open("./test.txt","r")
x = filehandle.readlines()
y = filehandle.read()
print (x)
print (y)
