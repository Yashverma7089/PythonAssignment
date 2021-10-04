# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.  
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

L = ['p','q']
L1 = []
n = int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in L:
        # L1.append("{}{}".format(j,i))
        # L1.append("%s%d"%(j,i))
        L1.append(j+'%d'%(i))
print(L1)