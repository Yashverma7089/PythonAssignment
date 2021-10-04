# Write a Python program to check a list is empty or not.  

L = []
n = int(input("Enter the value of n : "))
for i in range(n):
    v = int(input("Enter Element : "))
    L.append(v)
print("List :",L)

if len(L) == 0:
    print("List is empty")
else:
    print("List is not empty")