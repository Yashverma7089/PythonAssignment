# Write a Python program to get the frequency of the elements in a list.  

# L1 = [3,4,2,2,5,1,5,6,3]
# L2 = []
# for i in L1:
#     if i not in L2:
#         L2.append(i)
# L2.sort()
# for i in L2:
#     count = L1.count(i)
#     print("The frequency of",i,"is :",count)

L1 = [3,4,2,2,5,1,5,6,3]
S = list(set(L1))
for i in S:
    count = L1.count(i)
    print("The frequency of",i,"is :",count)