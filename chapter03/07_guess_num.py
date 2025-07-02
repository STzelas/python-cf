import random

def get_user_guess() -> None:
  """
  Propts user to insert a 'guess' which is a valid integer.
  """
  while True:
    try:
      return int(input("Please give an int: "))
    except ValueError:
      print("Invalid input, please enter a valid integer.")

def check_guess(secret:int, guess:int) -> None:
  """
  Checks if the guess by a user is the same a secret integer.

  secret (int): The secret number which the user must find.
  guess (int): The 'guess'(a valid integer) of the user.
  """
  if guess == secret:
    print("Bingo! Secret number: ", secret)
    return True
  elif abs(secret - guess) <= 5:  # με abs φευγει το πρόστιμο δίνει το absolute
    print("Hot")
  else:
    print("Cold")
  return False


def main():
  secret_number = random.randint(1, 10)
  MAX_TRIES = 5
  tries = 0

  # Ξεκινάει απο το 0 -> άρα έχουμε 5 προσπάθειες
  while tries < MAX_TRIES:
    guess = get_user_guess()
    if check_guess(secret=secret_number, guess=guess):
      break
    tries += 1
    if tries == MAX_TRIES:
      print("You reached the max number of tries")

if __name__ == "__main__":
  main()