# Write a Python program to find the highest 3 values in a dictionary.   

dict = {'3':5,'2':10,'1':25,'5':20,'4':25}
# dict={1:2,3:6,4:8,2:1,5:9}
L = sorted(list(dict.values()))
print(L[-1:-4:-1])

