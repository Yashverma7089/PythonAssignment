# Write a Python program to remove duplicates from Dictionary.   
dict = {'3':5,'2':10,'1':25,'5':20,'4':25}
temp = []
final_dict = {}
for key,value in dict.items():
     if value not in temp:
      temp.append(value)
      final_dict.setdefault(key,value)
print(final_dict)
