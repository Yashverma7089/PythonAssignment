# str = "A"
# while(str <= "Z"):
#     print(str, end=" ")
#     str = chr(ord(str) + 1)
# print()
# for i in range(26):
#     r = (i+13) % 26
#     str = chr(ord("A")+r)
#     print(str, end=" ")

# we can also solve this problem using this code
a = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
print("a:",a)
s = a[26:]+a[:26]
print("s:",s)