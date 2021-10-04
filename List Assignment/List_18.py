# Write a Python program to generate all permutations of a list in Python. 
import itertools
L = [1,2,3]
k = list(itertools.permutations(L))
print("All Permutations are :",k)