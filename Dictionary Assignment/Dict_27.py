# Write a Python program to convert a list into a nested dictionary of keys.   

# L1 = [1,2]
# dict = dict1 = {}
# for i in L:
#     dict1[i] = {}
#     dict1 = dict1[i]
# print(dict)

L1 = [1,2]
L2 = [{},{}]
dict2 = {}
for a,b in zip(L1,L2):
    dict1 = {a:b}
    dict2.setdefault(a,dict1)
print(dict2)