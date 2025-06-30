import re

# initialize my stack
# LIFO, Last in First out σαν στοίβα με βιβλία
stack = []

num = 0

# Γενικά είναι αφηρημένη προσέγγιση συγκριτικά με την
# java
# list.χχχχ(item) εδω κανείς δεν ξέρει τι είναι 
# αν είναι λίστα το list. αν βάλω όμως μετα πχ μια λίστα η 
# append θα λειτουργησει
# το append μπορεί να είναι οτιδήποτε, list.sotiris(item)
# 
def push(list:list, item: int) -> list:
  """
    Adds an item to a list and returns the item which was inserted.

    Args:
      list(list): The list the item will be inserted to
      item(int): The item you want to add in the list
  """
  list.append(item)  

def pop(list: list):
  """
    Removes the last item from a list and returns the removed value.

    Args:
      list(list): The list the item will be removed from.
  """
  if list:
    return list.pop()
  else:
    print("Stack is empty")

def print_stack(list: list):
  """
    Prints a list

    Args:
      list(list): The list you want to print
  """
  if list:
    print("Current state:", list)
  else:
    print("Stack is empty")

def print_menu():
  """
    Prints a menu of choices about a stack inserting and item,
    removing an item from the top, printing a stack and quiting
    the menu
  """
  print("1. Insert on top")
  print("2. Get from top")
  print("3. Print stack")
  print("4. q\Q for Quit")

def get_choice() -> str:
  """
    Returns an input prompt for a user to provide a choice
  """
  return input("Please provide your choice\n")

def main():
  choice = 0
  num = 0
  out_num = 0

  while True:
    print_menu()
    choice = get_choice()

    if not choice:
      continue

    if choice == 'q' or choice == 'Q' or choice == "4":
      break

    # row string literal σημαίνει το r μπροστά απο string
    pattern = r"^\d$" #regex (d αριθμός απο το 0 έως 9)  
    valid = re.match(pattern, choice)

    if not valid:
      print("Choice is not valid")
      continue
    # Τώρα ξέρω ότι θα είναι απο 0 έως 9 άρα κάνω ασφαλή typecast
    choice = int(choice)

    # Python 3.10+ επιτελεί την λειτουργία της Switch Case σε java
    match choice:
      case 1:
        num = input("Please insert a number: ")
        pattern = r"^\d+$"
        valid = re.match(pattern, num)
        if not valid:
          print("Error")
          continue
        num = int(num)
        # push on stack
        push(stack, num)
        print(f"{num} inserted")

      case 2:
        out_num = pop(stack)
        if out_num is not None:
          print("Item pop:", out_num)

      case 3:
        print_stack(stack)

      # default
      case _:
        print("Not valid choice. Try again.")


if __name__ == "__main__":
  main()