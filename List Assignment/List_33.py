# Write a Python program to generate all sublists of a list.  

L = []
n = int(input("Enter the size of list : "))
for i in range(n):
    v = int(input("Enter element : "))
    L.append(v)
print(L)

B = [[]]
for i in range(len(L)+1):
    for j in range(i):
        B.append(L[j:i])
print("Sublist of List=",L,"is :",B)