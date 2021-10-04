# Write a Python program to flatten a shallow list.  

L = []
n = int(input("Enter the number of list you want to insert in L : "))
for i in range(n):
    L1 = []
    n1 = int(input("Enter the number of  elements you want to insert in sublist : "))
    for j in range(n1):
        v = int(input("Enter value in %d sublist : "%(i)))
        L1.append(v)
    L.append(L1)
print("Input List :",L)

L2 = []
for l in L:
    for i in l:
        L2.append(i)
print("Final List is :",L2)