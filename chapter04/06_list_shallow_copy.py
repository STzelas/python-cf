my_list = [1, 2, "Hello", [3, 4, 5]]

def main():
  new_list = my_list[:]

  print(f"Are new_list and my_list the same object: {my_list is new_list}")
  print(id(my_list))
  print(id(new_list))

  my_list[0] = 100

  print(f"Original list: {my_list}")
  print(f"Shallow copy list: {new_list}")

  my_list[3][0] = 300
  print(f"Original list (2): {my_list}")
  print(f"Shallow copy list (2): {new_list}")

if __name__ == "__main__":
  main()