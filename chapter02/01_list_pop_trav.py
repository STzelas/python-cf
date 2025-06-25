# List populate and traverse
ages = [19, 23, 15, 55, 34, 19]  # Είναι list αυτό όχι array

print("Initial list of ages", ages)

for age in ages:
  print(age, end=", ",)
print()

# Η enumarate επιστρέφει ένα index και δίπλα το value
# άρα 0 - 19, 1 - 23 κλπ (ξεκινάει απο το 0)
# Η enumarate επίσης ξεκινάει απο default 0, αλλά
# μπορούμε να το αλλάξουμε κιολας.
# Μας εξυπηρετεί που είναι 0 τώρα επειδή το list είναι 0 index
# αλλα δεν καταλαβαίνει αντιστοίχηση με αυτή την έννοια
for index, value in enumerate(ages, 1):  
  print(f"Index: {index}, Value: {value}")
