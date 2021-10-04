# Write a Python program to print the numbers of a specified list after removing even numbers from it.  

L = []
n = int(input("Enter the number of elements : "))
for i in range(n):
    v = int(input("Enter %d element : "%(i+1)))
    L.append(v)
print(L)
l = []
for i in L:
    if i%2 != 0:
        l.append(i)
L= l.copy()
print(L) 

# L=[]
# n=int(input("Enter number : "))
# for i in range(n):
#     v=int(input("Enter value : "))
#     L.append(v)
# print(L)
# l=[]
# for i in L:
#     if(i%2==1):
#         l.append(i)
# print(l)