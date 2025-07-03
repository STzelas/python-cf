# Password generator
import string
import random

# str to list
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
# print(characters)

def generate_password():
  """
  Generate a random password based on the user-specified length
  """
  try:
    password_length = int(input("Give the password length: "))

    if password_length <= 0:
      print("Password length must be positive number.")
      return
  except ValueError:
    print("Invalid input. Please provide a positive integer.")

  random.shuffle(characters)

  password = []

  for i in range(password_length):
    password.append(random.choice(characters))
  
  random.shuffle(password)

  # list to str
  password = "".join(password)
  print(f"Generated password: {password}")

def main():
  while(True):
    option = input("\nDo you want to create a password? (yes/no)")

    if option.lower() == 'yes':
      generate_password()
    elif option.lower() == 'no':
      print('Goodbye!')
      break
    else:
      print("Wrong input")
      
if __name__ == "__main__":
  main()