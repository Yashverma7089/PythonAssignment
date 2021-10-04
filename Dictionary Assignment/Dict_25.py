# Write a Python program to print a dictionary in table format.   
dict = {1: ["Samuel", 21, 'Data Structures'], 2: ["Richie", 20, 'Machine Learning'], 3: ["Lauren", 21, 'OOPS with java']}
print("Name \t Age \t Course")
for value in dict.values():
    print("{} \t {} \t {}".format(value[0],value[1],value[2]))