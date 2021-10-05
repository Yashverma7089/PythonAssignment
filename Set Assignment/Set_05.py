# Write a Python program to remove an item from a set if it is present in the set.       
set = {1,2,5,3,6,7,9}
element =  int(input("Enter element you want to remove from the set : "))
if element in set:
    set.discard(element)
    print(element,"has been removed from the set",set)
else:
    print(element,"does not exist in set",set)