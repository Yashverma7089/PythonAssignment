# Write a Python script to add a key to a dictionary.   
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict = {0: 10, 1: 20}
key = int(input("Enter Key : "))
value = int(input("Enter Value : "))
dict.setdefault(key,value)
print(dict)