# Write a Python program to select the odd items of a list.  

L = [1,4,3,6,7,8,9]
odd_items = []
for i in L:
    if i%2 != 0:
      odd_items.append(i)
print("Odd Items are :",odd_items) 