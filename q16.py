#The data element contains a line from an /etc/shadow file. The shadow file is a colon delimited file.  The 2nd field in the colon delimited field contains the password information.   The password information is a dollar sign delimited field with three parts.  The first part indicates what cypher is used.  The second part is the password salt.  The last part is the password hash.   Retrieve the password salt for the root user.
#
import local_pyWars as pyWars
game = pyWars.exercise()
y = game.data(16)
print(y)
split1 = y.split('$')
print(split1)
x = split1[2]

game.answer(16,x)
print (game.score())
