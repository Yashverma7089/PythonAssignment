# Write a Python program to sum all the items in a list.  

L = []
n = int(input("Enter the value of n : "))
for i in range(n):
    v = int(input("Enter Element : "))
    L.append(v)
print("Sum is :",sum(L))