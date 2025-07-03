def my_add(a: float | int, b: float | int) -> float | int:
  """
  Adds two numbers and returns the result.

  Args:
    a (int, float): The first number to add.
    b (int, float): The second number to add.

  Returns:
    int | float: The sum of 'a' and 'b'.

  Raise:
    TypeError: If either 'a' or 'b' is not an integer or float.
  """
  # κανουμε check το type με isinstance με tuple of classes
  if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):  
    raise TypeError("Both a and b must be integers or floats.")
  return a + b
  pass

def main():
  print(my_add(10, 20.5))
  print("-" * 20)
  try:
    print(my_add("Hello", 10))
  except TypeError as err:
    print(err)

  print("-" * 20)
  print("Annotations:", my_add.__annotations__)
  print("-" * 20)
  print("Docs:", my_add.__doc__)
  print("-" * 20)
  help(my_add)

if __name__ == "__main__":
  main()