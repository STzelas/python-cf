# list manipulation
# Ordered list
fruits = ["Apple", "Orange", "Banana", "Apple"]

print(f"Initial list: {fruits}")

# Add a fruit at the end of the list
fruits.append("Berry")

print(f"After adding berry: {fruits}") 

# με append ['Apple', 'Orange', 'Banana', 'Apple', 'Berry', ['Grapes', 'Fig']]
# Για αυτό βάζω extend
fruits.extend(["Grapes", "Fig"])  

print(f"After adding grapes, fig: {fruits}")

# insert an element in a specific position
fruits.insert(1, "Coconut")
print(f"After adding coconut: {fruits}")

# update the first element
fruits[0] = "Melon"
print(f"After updating: {fruits}")

# Updating a slice of list ()
fruits[1:3] = ["A", "B", "C"]  # μπορούμε και A, B, C, D ,F ... όσα θέλουμε.
print(f"After updating slice: {fruits}")

print("------------------")
# Με .pop()
removed_item = fruits.pop()
print(f"Removed item: {removed_item}" )  # το pop το κρατάει
print(f"After pop {fruits}")

# remove 
fruits.remove("C") # παίρνει value
print(f"Afte remove 'C': {fruits}")

# fruits.remove("D")
# print(f"Afte remove 'D': {fruits}")

idx = fruits.index("A")
print(idx)

item_to_remove = "Grapesss"

if(item_to_remove in fruits):
  fruits.remove(item_to_remove)
  print(f"{item_to_remove} removed")
else:
  print("Fruit not found. Insert a valid fruit to remove")
  