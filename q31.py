#Data contains a dictionary of dictionaries.  The outer dictionary contains dates in the format of Month-Year.  The value for each of those entries is another dictionary.
#That dictionary contains Operating System classes as the key and its percentage of use in the target organization as the value.  What percentage of the attack surface was 'Vista' in '6-2017'?

import local_pyWars as pyWars
game = pyWars.exercise()
a = game.data(31)
b = dict(a['6-2017'])


game.answer(31,(b['Vista']))
print (game.score())
