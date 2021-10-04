# Write a Python program to find the second smallest number in a list.  

L1 = [3,4,2,2,5,3]
L2 = []
for i in L1:
  if i not in L2:
     L2.append(i)
L2.sort()
print("The second smallest number is :",L2[1])