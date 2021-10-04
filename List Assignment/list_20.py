#  Write a Python program access the index of a list.  

L = []
n = int(input("Enter the value of n : "))
for i in range(n):
    v = int(input("Enter Value : "))
    L.append(v)

for i in range(n):
    print("index :",i," & value :",L[i])