# Write a Python program to create a dictionary from two lists without losing duplicate values.   
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
    
L1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
L2 = [1, 2, 2, 3]
dict = {}
for i,j in zip(L1,L2):
    dict.setdefault(i,{j})
print(dict)
