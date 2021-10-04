# Write a Python program to generate and print a list except for the first 5 elements, 
# where the values are square of numbers between 1 and 30 (both included).  

L = []
for i in range(1,31):
    L.append(i**2)
print(L[5:])