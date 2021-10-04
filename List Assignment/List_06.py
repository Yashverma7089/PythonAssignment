# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.  
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


L = []
n = int(input("Enter the number of tuple : "))
for i in range(n):
    t = ()
    v1 = int(input("Enter First Number in Tuple : "))
    v2 = int(input("Enter Second Number in Tuple : "))
    t = t+(v1,v2,)
    L.append(t)
print(L)
sorted(L[:][1])
print(L)

# Other ways to make this program 
'''
L1 = []
n = int(input("Enter the number of tuple : "))
for i in range(n):
    t = ()
    v1 = int(input("Enter First Number in Tuple : "))
    v2 = int(input("Enter Second Number in Tuple : "))
    t = t+(v1,v2,)
    L1.append(t)
print(L1)
for j in range (1,len(L1)) :
  for i in range(len(L1)-j) :
    if L1[i][1]>L1[i+1][1] :
      temp=L1[i]
      L1[i]=L1[i+1]
      L1[i+1]=temp
print("Sorted List :",L1)
'''

'''
L1 = []
n = int(input("Enter the number of tuple : "))
for i in range(n):
    t = ()
    v1 = int(input("Enter First Number in Tuple : "))
    v2 = int(input("Enter Second Number in Tuple : "))
    t = t+(v1,v2,)
    L1.append(t)
print(L1)
L2 = []
for i in L1:
    L2.append(i[1])
L2.sort()

L3 = []
for i in range(len(L2)):
  for j in range(len(L1)):
    if L2[i] == int(L1[j][1]):
       L3.append(L1[j])
       L1.pop(j)
       break
print("Sorted List :",L3)       
'''

'''
L1 = []
n = int(input("Enter the number of tuple : "))
for i in range(n):
    t = ()
    v1 = int(input("Enter First Number in Tuple : "))
    v2 = int(input("Enter Second Number in Tuple : "))
    t = t+(v1,v2,)
    L1.append(t)
print(L1)
L2 = []
for i in L1:
    L2.append(i[1])
L2.sort()

L3 = []
for l in L2:
  for T in L1:
    if l == int(T[1]):
       L3.append(T)
       L1.remove(T)
       break
print("Sorted List :",L3) 
'''
