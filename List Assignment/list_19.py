# Write a Python program to get the difference between the two lists.  

L1 = [10,15,20,25,30,35,40]
L2 = [15,25,35,13]
for i in L2:
  if i in L1:
    j = L1.index(i)
    L1.pop(j)
print("Difference between Two List :",L1)