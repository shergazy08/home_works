# import random
#
# a=random.randint(0,100)
#
# from random import randint
#
# s=randint(0,10)
#
# import datetime as dt
#
# nov=dt.datetime.now()
#
# from random import *
#
# randint(0,10)
from pydoc import stripid

# import model
#
#
# # model.last_sum(15, 5)
#
# last=input('tanda: ').strip().lower()
# print(model.great(a))
#

import model

print(model.add_user('Аида'))
print(model.get_user())
print(model.delete_user('Аида'))
print(model.get_user())


