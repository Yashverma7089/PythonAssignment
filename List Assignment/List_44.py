# Write a Python program to generate groups of five consecutive numbers in a list.  

n = int(input("Enter how many consecutive numbers you want to print : "))
L = []
for i in range(n):
    L1 = []
    for j in range(1,6):
        L1.append(5*i + j)
    L.append(L1)
print("List of Consecutive Numbers is :",L)