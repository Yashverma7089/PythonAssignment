# Write a Python program to print a dictionary line by line.   

my_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print("key \t Value")
for key in my_dict.keys():
    print(key, "\t", my_dict[key])