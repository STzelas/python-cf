def compare_list(list1: list, list2: list) -> None:
  """
  Compares two lists for identity and equality.

  Args:
    list1 (list): The first list to compare.
    list2 (list): The second list to compare.

  Returns: None
  """
  # βάζω το keyword is, πρέπει να έχουν δηλαδή το
  # ίδιο id (μνήμη), να ταυτίζονται
  # identity check ->  list1 is list2
  print(f"{list1} is {list2}: {list1 is list2}")

  # checkarei αν τα περιεχόμενα είναι τα ίδια
  # equality check ->  list1 == list2
  print(f"{list1} == {list2}: {list1 == list2}")


def main():
  my_list = [1, 2, 3]
  your_list = [1, 2, 3]

  new_list = my_list

  # compare lists
  compare_list(my_list, your_list)
  print(id(my_list))
  print(id(your_list))
  print(id(new_list))
  


if __name__ == "__main__":
  main()