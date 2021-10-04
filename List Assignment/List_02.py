# Write a Python program to multiplies all the items in a list.  

L = []
n = int(input("Enter the value of n : "))
for i in range(n):
    v = int(input("Enter Element : "))
    L.append(v)
print("List :",L)
mul = 1
for i in L:
    mul *= i
print("Product is :",mul)