# . Write a Python program to find missing and additional values in two lists.  
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

L1 = [1,2,3,4,5]
L2 = [1,4,5,6,7,9]

missing_element = []
additional_element = []
for i in L1:
    if i not in L2:
        missing_element.append(i)

for i in L2:
    if i not in L1:
        additional_element.append(i)

print("Missing Element :",missing_element)
print("Additional Element :",additional_element)