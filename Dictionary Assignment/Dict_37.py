# Write a Python program to replace dictionary values with their sum.   

d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : [34,3],
        'C' : [12,34,66],
        'D' : [7, 8, 9, 6, 4] }

dict = {}
for key,value in d.items():
    dict.setdefault(key,sum(value))
print(dict)