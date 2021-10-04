# Write a Python program to sort a list of nested dictionaries.  

L = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
new_list = []
for i in range(len(L)-1):
    if L[i]['key']['subkey'] > L[i+1]['key']['subkey']:
        temp = L[i]['key']['subkey']
        L[i]['key']['subkey'] = L[i+1]['key']['subkey']
        L[i+1]['key']['subkey'] = temp
    
print(L)