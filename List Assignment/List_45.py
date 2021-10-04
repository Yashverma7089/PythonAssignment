# Write a Python program to convert a pair of values into a sorted unique array.  

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
L1 = []
for i in L:
    for j in i:
      if j not in L1:
         L1.append(j)
print(L1)

