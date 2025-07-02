# Immutability
# Επιστρέφει το id του variable με την built-in id()
def print_id(variable_name, variable):
  print(f"id({variable_name}) = ({id(variable)})")

def main():
  original_list = [1, 2]
  print_id("0", original_list[0])
  print_id("1", original_list[1])
  new_list = original_list

  print_id("original_list", original_list)
  print_id("new_list", new_list)

  new_list[0] = 100

  print("-------")
  print(original_list)
  print(new_list)


  # είναι άλλη λίστα δεν θα έχουν ίδια id με την new list
  temp_list = [100, 2]
  print_id("temp_list", temp_list)


  # Αλλάζει το id (δηλαδή το σημείο στην μνημη) του πρώτου στοιχείου.
  # Το 10 υπάρχει αλλα το πρώτο στοιχείο δείχνει τώρα στο 100
  print_id("0", original_list[0])
  print_id("1", original_list[1])
  print_id("new list", new_list)
  # Θα βγάλει το ίδιο λόγω immutability. Δημιουργείται νέα λίστα
  # και δείχνει πάλι στο 100 που υπάρχει μέσα στην παλιά
  print_id("original list item 0", original_list[0])
  print_id("temp list item 0", temp_list[0])


if __name__ == "__main__":
  main()