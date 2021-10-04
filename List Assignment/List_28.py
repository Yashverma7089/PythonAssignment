# Write a Python program to find the second largest number in a list.  

L1 = [3,4,2,2,5,5,6,3]
L2 = []
for i in L1:
  if i not in L2:
     L2.append(i)
L2.sort(reverse=True)
print("The second largest number is :",L2[1])