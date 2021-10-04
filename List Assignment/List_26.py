# Write a python program to check whether two lists are circularly identical

L1=[1,2,4,6]
L2=[6,4,2,3]
L1.sort()
L2.sort()
if L1==L2:
    print("true")
else:
    print("false")
    
# L1 = [1,2,4,5,3]
# L2 = [2,1,5,3,4]
# L1.sort()
# L2.sort()
# if L1[:] == L2[:]:
#   print("Lists are Circularly identical")
# else:
#   print("Lists are not Circularly identical")

# L1 = [1,2,4,5,3]
# L2 = [2,1,6,3,4]
# L1.sort()
# L2.sort(reverse=True)
# if L1[:] == L2[-1:]:
#   print("Lists are Circularly identical")
# else:
#   print("Lists are not Circularly identical")
