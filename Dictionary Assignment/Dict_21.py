# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.   
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

# dict = {'1':['a','b'], '2':['c','d']}
# for i in dict['1']:
#     for j in dict['2']:
#         print(i+j)

from itertools import product
dict = {'1':['a','b'], '2':['c','d']}
for i,j in product(*dict.values()):
   print(i+j)