# Write a Python program to check whether a list contains a sublist.  

List = [1,2,3,4,5,6,7,8,9,10]
sublist = [1,2,5,4,11]
count = 0
for i in sublist:
    if i in List:
       count += 1

if len(sublist) == count:
    print("True,",sublist,"is present in",List)
else:
    print("False,",sublist,"is not present in",List)