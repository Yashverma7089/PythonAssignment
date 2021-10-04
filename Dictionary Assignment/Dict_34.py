# Write a Python program to count number of items in a dictionary value that is a list

d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : [12,34,66],
        'D' : [7, 8, 9, 6, 4] }
sum = 0
for  value in d.values():
    if isinstance(value, list):
       sum += len(value)
print(sum)
