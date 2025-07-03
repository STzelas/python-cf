def name_space(num):
  if not isinstance(num, int): # Αντί για error handling me try except. ελέγχω με isinstance()
    print("The num must be integer")
    return
  
  if num < 0:
    print("The num of spaces must be positives.")
    return
  
  name = input("Please enter your name: ").strip()  # σαν την trim στην java

  if not name:
    print("No name provided.")
    return
  
  spaced_name = (" " * num).join(name)
  print(spaced_name)

def main():
  try:
    num = int(input("Please enter the number of spaces between the characters."))
    name_space(num)
  except ValueError:
    print("Invalid input")

if __name__ == "__main__":
  main()