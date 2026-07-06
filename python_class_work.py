###### MOdule in python
# 1 built in module
# 2 user defined module
# 3 External module

############## importing method
# 1 simple import 
# import scikit_learn

# 2 import with alis 
# import scikit_learn as sk

# 3 import for specific

from pandas import DataFrame

##########################################################

# operating management system
import os

print(os.cpu_count())
print(os.listdir())
# print(os.fdopen())




def resturant_bill(oder):
  rate = 0
  if oder == "birayani":
    print(f"rate is 300")

  elif oder == "qourma":
    print("rate is 1000")

  else:
    print("we have not that item in menu ")


obj = resturant_bill("birayani")
print(obj)




### Lottery system

import random
for i in range(5):
  random_num = random.randint(100,200)
  print(f"Random number is:{random_num}")
