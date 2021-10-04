# Write a Python program to remove duplicates from a list. 

L1 = []
n = int(input("Enter the number of elements : "))
for i in range(n):
    v = int(input("Enter %d string : "%(i+1)))
    L1.append(v)
print("List before removing duplicates :",L1)

L2 = []
for i in L1:
    if i not in L2:
        L2.append(i)
print("List after removing duplicates :",L2)