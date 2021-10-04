# Write a Python program to sort Counter by value.   
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

from collections import Counter
dict1 = {'Math':81, 'Physics':83, 'Chemistry':87}
print(dict(Counter(dict1)))