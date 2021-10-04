# Write a Python program to remove spaces from dictionary keys.   
# Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS','P 0 3 ': 'Soft Computing'}
# New dictionary :  {'P01': 'DBMS', 'P03': 'Soft Computing', 'P02': 'OS'}

Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS','P 0 3 ': 'Soft Computing'}
dict = {}
for key,value in Product_list.items():
    dict.setdefault(key.translate({32: None}),value)
print(dict)

# translate({key:value}) function : The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.