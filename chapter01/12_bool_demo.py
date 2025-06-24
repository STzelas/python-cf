# Booleans
a = True
b = False

print(type(a), b, sep=", ")
print(type(b), a, sep=", ")

# Short circuit

result = a or b
print(result)

 # Τα bool στην Python είναι σαν class τον 
 # integer οπότε το False αντιστοιχεί στο 0,
 # και το True στο 1
print("True + True =", True + True) # 2
print(True * 5) # 5 