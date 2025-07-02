def is_square(length: int, width: int) -> bool:
  """
  Checks if a rectangle is a square

  Args:
    length (int): length of the rectangle.
    width (int): width of the rectangle.
  
  Returns:
    bool: True if the rectangle is square, False otherwise.
  """
  return length == width

def main():
  
  # Δεν έχει scope η try,
  # σαν το try catch
  try:
    length = int(input("Please enter the length of the rectangle: "))
    width = int(input("Please enter the width of the rectangle: "))
  except ValueError:
    print("Invalid input. Please enter 2 ints.")
    return

  if is_square(length, width):
    print("The rectangle is square.")
  else:
    print("The rectangle is not square.")

if __name__ == "__main__":
  main()