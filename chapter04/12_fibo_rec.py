def fibo(n: int) -> int:
  """
  Takes a given number and returns it's fibonacci number.

  Args:
    n (int): The number which is given to get the fibonnaci number.

  Raises:
    ValueError in case the user does not enter a valid integer. 
  """
  # fibo(n) = fibo(n - 1) + fibo(n - 2)
  # fibo(0) = 0
  # fibo(1) = 1
  return n if n in (0, 1) else (fibo(n-1) + fibo(n-2))

def main():
  try:
    n = int(input("Please enter a valid integer: "))
  except ValueError:
    print("Invalid input.")
    return
  print(f"Fibo({n}) = {fibo(n)}")

if __name__ == "__main__":
  main()