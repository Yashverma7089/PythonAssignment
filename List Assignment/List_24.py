# Write a Python program to append a list to the second list.  

L1 = []
L2 = []
n = int(input("Enter the size of list : "))
for i in range(n):
    v = int(input("Enter element at %d position : "%(i+1)))
    L1.append(v)
print("First List :",L1)

n = int(input("Enter the size of list : "))
for i in range(n):
    v = int(input("Enter element at %d position : "%(i+1)))
    L2.append(v)    
print("Second List :",L2)
print("List after appending :",L1+L2)