# . Write a Python program to change the position of every n-th value with the (n+1)th in a list.  
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

L = [0,1,2,3,4,5]
for i in range(0,len(L),2):
    temp = L[i]
    L[i] = L[i+1]
    L[i+1] = temp
print(L)
