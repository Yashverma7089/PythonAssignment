# Write a Python program to check multiple keys exists in a dictionary.   

d={"Mon":3, "Tue":11,"Wed":6,"Thu":9}
s1 = {"Tue","Thu"}
if (d.keys()) >= s1:
    print("All keys are present in dictionary")
else:
    print("All keys are not present in dictionary")

s1 = {"Fri","Mon"}
if (d.keys()) >= s1:
    print("All keys are present in dictionary")
else:
    print("All keys are not present in dictionary")

