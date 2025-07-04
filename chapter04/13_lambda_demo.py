def my_power(base: int, exp: int) -> int:
  """
  Takes a base number and a number to power it to and returns the result.

  Args:
    base (int): The base number.
    exp (int): The number which the base number will be powered to

  Returns:
    int: The result
  
  Raises:
    ValueError in case the user does not enter a valid integer. 
  """
  return base ** exp

# Το ίδιο πράμα με παραπάνω done with lambda
# Το base, exp αντιπροσοπεύει τα ορίσματα
# μετα την : επιστρέφει (υπονοείται return)
# base ** exp
power_to = lambda base, exp: base ** exp  

def main():
  try:
    base = int(input("Please enter an integer for the base number: "))
    exp = int(input("Please enter an integer for the power: "))
  except ValueError:
    print("Invalid input.")
    return
  
  print(my_power(base, exp))

  print(power_to(2, 10))



if __name__ == "__main__":
  main()