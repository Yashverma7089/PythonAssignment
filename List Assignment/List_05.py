#  Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

L = []
n = int(input("Enter the number of string : "))
for i in range(n):
    v = input("Enter %d string : "%(i+1))
    L.append(v)
print(L)
count = 0
for i in L:
    if(len(i) >= 2 and i[0] == i[len(i)-1]):
        count += 1
print("Total Count is :",count)