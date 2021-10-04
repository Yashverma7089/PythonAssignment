text = input("Enter any string : ")
text.lower()
vowel = ['a','e','i','o','u']
for v in vowel:
    count = 0
    for t in text:
      if(t == v):
          count += 1
    print(v,"comes",count,"times")
