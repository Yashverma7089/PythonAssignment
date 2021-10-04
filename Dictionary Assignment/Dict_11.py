# Write a Python program to multiply all the items in a dictionary.   
dict = {'1':5,'2':10,'3':15,'4':20,'5':25}
L = list(dict.values())
mul = 1
for i in L:
    mul *= i
print("Multiply is :",mul)