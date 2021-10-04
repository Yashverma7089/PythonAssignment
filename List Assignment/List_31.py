# Write a Python program to count the number of elements in a list within a specified range.  
L = [3,4,2,2,5,1,5,6,3]
n1 = int(input("Enter the value of n1 : "))
n2 = int(input("Enter the value of n2 : "))
count = 0
for i in L:
    if i >= n1 and i <= n2:
      count += 1
print("Total elements in range(%d,%d) are %d"%(n1,n2,count)) 