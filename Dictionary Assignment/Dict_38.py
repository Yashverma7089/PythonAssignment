#  Write a Python program to match key values in two dictionaries.   
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}
for key,value in dict1.items():
    if (key,value) in dict2.items():
        print(key,":",value,"is present in both dictionaries")