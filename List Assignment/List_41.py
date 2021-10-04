# Write a Python program to create multiple lists.  

L = []
row = int(input("Enter number of list you want to insert : "))
for i in range(row): 
    temp = []
    col = int(input("Enter number of elements you want to insert in sublist : "))
    for j in range(col):
        v = int(input("Enter element at [%d][%d] : "%(i+1,j+1)))
        temp.append(v)
    L.append(temp)
print("Multiple List is :",L)
