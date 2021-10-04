# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.   

n = int(input("Enter the value of n : "))
d = {}
for i in range(n): 
    key = input("Enter key : ")
    value1 = int(input("Enter the value1 : "))
    value2 = int(input("Enter the value2 : "))
    d.setdefault(key,list(range(value1,value2)))
print(d)

for value in d.values():
    print(value[4])

for key,value in d.items():
    print(key,"has value",value)
