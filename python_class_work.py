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
########### 7/7/2026



# string
def department_name(name):
  n = name + " quest"
  print(f"Department is : {n}")

print(department_name("cs"))



# int 
def add_num(num):
  n = 3
  n += num
  print(f"Addition of number is :{n}")

print(add_num(6))



# tuple 
def my_collection(a):
  item = ("hello","Rabia",1,2,3,4)
  item += (a,)
  print(f"My tuple is :{item}")

print(my_collection(33))



def fruits_list(my_list :list):
  list1 = ["cs"]
  list1.append(my_list)
  print(f"All item in my list:{list1}")

print(fruits_list(["AI","quest"]))
