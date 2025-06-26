# Sets {} - modifiable - unordered σαν μια τσαντα πχ - δεν έχω διπλότυπα
bag = {"eggs", "oranges", "bananas"}
print(f"Initial bag: {bag}, Type: {type(bag)}")

# add a new item
# Εκτυπώνονται σε τυχαια θέση
# Αν βάλεις κάποιο που υπάρχει
#  δεν βγάζει ερρορ απλά δεν κάνει
#  τίποτα
bag.add("apples")
print(f"Bag after adding bananas: {bag}")

# remove
# αν βγάλεις κάτι που δεν υπάρχει
# βγάζει key error! οχι value error
# τα λεξικά ειναι hash key-value pairs
# τα σύνολα(Sets) είναι σαν μόνο τα κλειδιά
# απο ένα λεξικό
bag.remove("bananas")
print(f"Bag after removing bananas: {bag}")

# Τα Sets είναι iterable objects, απλά δεν είναι ordered
for item in bag:
  print(item, end=", ")
print()