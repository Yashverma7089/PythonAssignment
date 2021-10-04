# Write a Python program to find the index of an item in a specified list.  

L = ['G','w','a','l','i','o','r']
i = input("Enter element you want to know index : ")
try:
    S = L.index(i)
    print("The index of",i,"is :",S)
except Exception as e:
    print("Error :",e)