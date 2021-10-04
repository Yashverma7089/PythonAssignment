# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.  
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

L=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a=L[0]
b=L[4]
c=L[5]
L.remove(a)
L.remove(b)
L.remove(c)
print("L:",L)

# L = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# L1= []
# for i in range(len(L)):
#     if(i not in [0,4,5]):
#         L1.append(L[i])
# print(L1)