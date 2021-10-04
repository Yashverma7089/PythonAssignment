# Write a Python program to find the list of words that are longer than n from a given list of words.  

L1 = ["Peacock","Mango","Orange","Rabbit","Dangerous","Gorgeous","Healthy","Beautiful"]
n = int(input("Enter the value of n : "))
print("L1 :",L1)
L2 = []
for i in L1:
    if len(i) > n:
        L2.append(i)
print("L2 :",L2)