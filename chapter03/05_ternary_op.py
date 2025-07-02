def compare_integers(a: int, b: int) -> None:
  """
  Compares two integers for identity and equality.

  Args:
    a (int): The first int to compare.
    b (int): The second int to compare.
  """
  if a == b:
    print("The numbers are equal")
  elif a > b:
    print(f"Number a: {a} is greater than b: {b}")
  elif a < b:
   print(f"Number a: {a} is less than b: {b}")


def main():
  try:
    a = int(input("Please enter the first number to compare: "))
    b = int(input("Please enter the second number to compare: "))
    
    # compare_integers(a, b)
  except ValueError:
    print("Invalid input. Please insert valid integers")

  # 1. Simple example of ternary operator
  if a > 0:
    print("positive")
  else:
    print("non-positive")

  result = "positive" if a > 0 else "non-positive"
  print(result)
  # print("positive" if a > 0 else "non-positive")
  
  # 2. Extended example of ternary operator
  result = (
    "The numbers are equal" if a == b else
    f"Number a: {a} is greater than b: {b}" if a > b else
    f"Number a: {a} is less than b: {b}"
  )
  print(result)


if __name__ == "__main__":
  main()