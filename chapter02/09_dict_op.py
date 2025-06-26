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

# read an element (access)
# product_1 = products[1]
# print(product_1)
# key-error δεν υπάρχει 10
# product_10 = products[10]
# print(product_10)
product_10 = products.get(10, "Out of stock")
print(product_10)