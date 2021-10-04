# Write a Python program to convert list to list of dictionaries.  
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

L = [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]
L1 = []
for i in range(len(L)):
  for j in range(len(L[i])):
    dict = {}
    dict['color name'] = L[i][j]
    dict['color code'] = L[i+1][j]
    L1.append(dict)
  break
print(L1)