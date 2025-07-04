# Factorial recursive

def factorial(n: int) -> int:
  """
  Gives the factorial value of a given number.

  Args:
    n (int): The number which the user gives

  Raises:
    ValueError in case the user does not enter a valid integer.
  """
  # Base cases: 0! = 1, 1! = 1
  return 0 if n < 0 else 1 if n in (0, 1) else n * factorial(n - 1)
  

def main():
  try:
    n = int(input("Please enter an integer: "))
  except ValueError:
    print("Invalid input")
    return
  print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
  main()