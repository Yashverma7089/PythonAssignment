# Write a Python program to add member(s) in a set.       
s = set()
n = int(input("Enter the size of set : "))
for i in range(n):
    element = int(input("Enter value : "))
    s.add(element)
print("Set is :",s)