# Write a Python program to clone or copy a list.  

L = []
n = int(input("Enter the value of n : "))
for i in range(n):
    v = int(input("Enter Element : "))
    L.append(v)
print("List :",L)
D = L.copy()
print("Copied List :",D)