# List , Μπορούμε και ανομοιογενή τύπους
items = [1, 2, 3.14, True, "Hello CF7"]

for item in items:
  print(item, end=" ")
print()

# Nested List
nest_list = [
  [1, 2],
  [3, 4],
  [5, 6]
]

# nest_list = [[1, 2], [3, 4], [5, 6]]

# Αν θέλουμε το πρώτο στοιχείο της λίστας
print(f"first list item: {nest_list[0]}")

# I want to get the '3' (as a two dim arr)
print(nest_list[1][0]) # 3

# [3, 4], [1, 2]
print(nest_list[1], nest_list[0], sep=", ")

print("-" * 20)

# slice - challenge
print(nest_list[1::-1])
