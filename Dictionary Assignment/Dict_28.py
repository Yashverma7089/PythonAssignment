# Write a Python program to sort a list alphabetically in a dictionary.   

L = {'n1':[2,6,3,1],'n2':[2,7,4,1,2],'n3':[4,2,5,1,7]}
dict = {}
for key, value in L.items():
    dict.setdefault(key,sorted(value))
print(dict)