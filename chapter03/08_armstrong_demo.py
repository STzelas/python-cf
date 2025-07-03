def is_armstrong_number(num) -> bool:
  """
  Checks if a number is an armstrong number.

  Args:
    n (int): The number you are checking.

  Return: True if it is and False otherwise.
  """
  digits = str(num)
  power = len(digits)
  total = 0

  for digit in digits:
    total += int(digit) ** power

  return num == total

def main():
  try:
    num = int(input("Please insert an int: "))
  except ValueError:
    print("Invalid input")
    return
  
  if is_armstrong_number(num):
    print(f"{num} is Armstrong number")
  else:
    print(f"{num} is not an Armstrong number")

  # return f"{num} is Armstrong number." if is_armstrong_number(num) else f"{num} is not an Armstrong number."

if __name__ == "__main__":
  main()