# Write a Python program to insert an element before each element of a list.  

L = ['apple','banana','papaya','guava']
element = input("Enter element which you want to insert before each element : ")
L1 = []
for i in L:
    L1.append(element)
    L1.append(i)
print(L1)