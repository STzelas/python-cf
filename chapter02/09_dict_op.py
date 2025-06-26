# Populate a dictionary as dict {} - hashed key-value pairs - modifiable - κλειδή - τιμή
products = {
  1:"apples",
  2:"bananas",
  3:"honey",
  4:"melon"
}
print(f"Initial dict: {products}, Type: {type(products)}")

# insert a new key:value pair
# Αν κάτι υπάρχει όταν κάνουμε insert
# τότε κάνει UPDATE!!
# πχ αν θες να μετρήσεις την συχνότητα
# εμφάνισης ενός αντικειμένου
# μέσα σε μία λίστα
# μπορείς να έχεις το ονομα του αντικειμένου ως key
# και ως value την συχνοτητα εμφάνισεις του
# μπορείς έτσι να το διασχίσεις και να 
# για κάθε ένα αντικείμενο βάλτο με εισαγωγή 1
# αν υπάρχει ξανά βάλτο με value + 1
products[3] = "orange"
print(f"Dict after insert: {products}")
print("---------------------")
# read an element (access)
# product_1 = products[1]
# print(product_1)
# key-error δεν υπάρχει 10
# product_10 = products[10]
# print(product_10)
product_10 = products.get(10, "Out of stock")
print(product_10)
print("---------------------")
# delete
del products[1] # κάνει delete το key:value pair
print(f"After deleting key 1 { products }")

removed_item = products.pop(10, "Item not found") # default value  στην pop σε περίπτωση που δεν υπάρχει το key
print(f"removed item: {removed_item}")
print(f"After removal: {products}")

print("---------------------")
# remove the 'last' inserted item with popitem()
key, value = products.popitem() # επιστρέφει μια πλοιάδα όπου το 1ο στοιχείο είναι int και το 2ο str
print(f"Key: {key}, Value: {value}")
print(products)

print("---------------------")
key_to_check = 2

if(key_to_check in products):
  print(f"Key {key} exists")
else:
  print(f"Key: {key_to_check} does not exist")

print("---------------------")
# iterate
for key in products:  # με in μέσα σε λεξικό κοιτάμε τα keys
  print(key, ":", products[key]) # αν θέλω το και το value ετσι
print("---------------------")
for key in products.keys(): # το ίδιο, καλύτερα έτσι για readability
  print(key, ":", products[key])

print("---------------------")
for value in products.values(): # Εκτυπώνω μόνο τα values
  print(value)

print("---------------------")
for key, value in products.items(): # Εκτυπώνω και τα keys και τα values
  print(key, ":", value)