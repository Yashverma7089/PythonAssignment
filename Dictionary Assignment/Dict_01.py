# Write a Python script to sort (ascending and descending) a dictionary by value.   

# dict = {}
# n = int(input("Enter the value of n : "))
# for i in range(n):
#     key = input("Enter Key : ")
#     value = int(input("Enter Value : "))
#     dict.setdefault(key, value)
# print(dict)

dict = {'1':4,'2':1,'3':5,'4':6}

L= list(dict.items())
L1 = []
for i in L:
    L1.append(list(i))

for i in range(len(L1)-1):
    for j in range(len(L1[i])-1):
        if(L1[i][j+1] > L1[i+1][j+1]):
            temp = L1[i]
            L1[i] = L1[i+1]
            L1[i+1] = temp

D = {}
for i in range(len(L1)):
    for j in range(len(L1[i])-1):
      D.setdefault(L1[i][j],L1[i][j+1])
print(D)
 