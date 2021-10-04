# Write a Python program to convert a list of multiple integers into a single integer.  
# Sample list: [11, 33, 50]
# Expected Output: 113350

L = [11,33,50]
new_list = ""
for i in L:
    new_list += str(i)
print(int(new_list))

# L = [11,33,50]
# L1= []
# for i in L:
#     L1.append(str(i))
# print(L1)
# k = "".join(L1)
# print(int(k))