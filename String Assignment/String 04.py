text = """How much wood would a woodchuck chuck If a woodchuck could chuck wood?

He  would  chuck ,  he  would ,  as  much  as  he  could ,

And  chuck  as  much  as  a  woodchuck  would

If  a  woodchuck  could  chuck  wood."""

str = text.lower()
txt = input("Enter word : ")
L = [txt, txt+'.',txt+'?',txt+","]
s = str.split()
count = 0
for txt in s:
    if txt in L:
        count += 1
print(count)
