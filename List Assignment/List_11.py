# Write a Python function that takes two lists and returns True if they have at least one common member.  

def check(L1,L2):
    for i in L1:
     if i in L2:
        print("True")
        break

L1 = [1,2,3]
L2 = [4,2,6]
check(L1,L2)

