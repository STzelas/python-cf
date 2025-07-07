# closure Που κάνει generate id για κάθε departmend

def department_id_generator(department):
  last_id = 0

  def generate_id():
    # όταν το προσθέσω αυτό δείχνω ότι η last id
    # που θα χρησιμοποιήσω μετά δεν είναι άλλη, είναι αυτή 
    # επειδή κανονικά δεν μπορεί να κάνει access την μεταβλητη
    nonlocal last_id 
    last_id += 1
    return f"{department}--{last_id}", last_id
  
  return generate_id # return συνάρτηση

def main():
  python_id_gen = department_id_generator("Python")
  android_id_gen = department_id_generator("Android")

  print(python_id_gen()) # ('Python--1', 1) είναι callable γιατι η department id generator επιστρέφει συνάρτηση
  print(python_id_gen()) # ('Python--2', 2) τα closures μαζί με την επιστροφή της συνάρτησης εμπερικλείεται και η τιμή της οποίας το value μένει σητν μνήμη

  print(android_id_gen())
  print(android_id_gen())

if __name__ == "__main__":
  main()