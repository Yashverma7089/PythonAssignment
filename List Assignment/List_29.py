# Write a Python program to get unique values from a list.  

L1 = [3,4,2,2,5,1,5,6,3]
L2 = []
for i in L1:
  if i not in L2:
     L2.append(i)
print("Unique Values are :",L2[:])