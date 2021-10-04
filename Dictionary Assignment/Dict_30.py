# Write a Python program to get the top three items in a shop.   
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

from collections import Counter
 
my_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
k = Counter(my_dict)
print(k) 
high = k.most_common(3)
print(high) 
for i in high:
    print(i[0]," :",i[1]," ")