# Write a Python program to get the largest number from a list.  

L = []
n = int(input("Enter the value of n : "))
for i in range(n):
    v = int(input("Enter Element : "))
    L.append(v)
print("List :",L)
print("Largest Number is :",max(L))