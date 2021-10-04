# Write a Python script to check if a given key already exists in a dictionary.   
    
dict = {'1':10,'2':20,'3':30,'4':40,'5':50}
key = input("Enter Key you want to check : ")
result = dict.get(key,'Not found')

if(isinstance(result,str)):
    print("Key Does not Exit in Dictionary")
else:
    print("Key Exit in Dictionary")
