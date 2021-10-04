# Write a Python program to generate a 3*4*6 3D array whose each element is *.  

n = int(input("Enter the number of arrays : "))
row = int(input("Enter the number of arrays : "))
col = int(input("Enter the number of arrays : "))
L = []
for i in range(n):
    L1 = []
    for j in range(row):
        L2 = []
        for k in range(col):
            L2.append('*')
        L1.append(L2)
    L.append(L1)
print(L)
# for i in range(n):
#     for j in range(row):
#         for k in range(col):
#            print(L[i][j][k], end=" ")
#         print()
#     print()
    