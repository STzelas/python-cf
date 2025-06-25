# range(10)

a = range(10)
print(f"Type of a : {type(a)}")  # type class range / δημιουργείται το object και ξέρει τι έχει μέσα

for i in range(10): # φέρνει δυναμικά όποιο αποτέλεσμα ζητείται!!! δεν διασχίζει και μετά φαίρνει
  if(i == 5):
    break
  print(i, end=" ")
print()

for i in range(10):
  if(i == 5):
    continue
  print(i, end=" ")
print()
print("-" * 10)

for i in range(10):
  if(i == 5):
    continue
  print(i, end=" ")
else:  # εκτελείτε όταν τελείωσει η loop
  print("Loop ended")

# List of fruits
fruits = ["Banana", "Orange", "Mango", "Apple"] # List

fruit_to_check = "Banana"

for fruit in fruits:
  if (fruit == fruit_to_check):
    print(f"Fruit to check is in the list")
    break
else:
  print(f"{fruit_to_check} not in list")

print("-" * 20)

# Happy hour
print("Why do Python devs never get lost?")
print("Because they always know where 'in' is!\n") # Πάρα πολλύ συχνά χρησιμοποιείται το in

# αντί για την παραπάνω for (much simpler)
if fruit_to_check in fruits:
  print(f"Fruit to check is in the list")
else:
  print(f"{fruit_to_check} not in list")

# challenge
print("One line example")
print(f"{fruit_to_check} is {'in' if  fruit_to_check in fruits else 'not in'} the list") # σαν να μιλάς κανονικά - pythonian προσέγγιση