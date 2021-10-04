# Write a Python program to find common items from two lists.  

L1 = [1,4,3,5,6,2]
L2 = [1,7,3,8]
L3 = []
for i in L1:
    if i in L2:
       L3.append(i)
print("Common elements from",L1,"and",L2,"is :",L3) 
