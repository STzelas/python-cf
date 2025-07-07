# generic abstract calculator
def calculator(n1, n2, operation):
  try:
    return operation(n1, n2)
  except TypeError as e:
    print(f"Error: {e}. Ensure the 'operation' argument is a function which takes 2 ints as args.")

def add(no1, no2):
  return no1 + no2

def multiply(no1, no2):
  return no1 * no2

def division(no1, no2):
  return no1 / no2

def sub(no1, no2):
  return no1 - no2

def main():
  print("Addition:", calculator(7, 9, add))
  print("Subtraction:", calculator(100, 40, sub))
  print("Multiplication", calculator(5, 4, multiply))
  print("Division:", calculator(10, 2, division))

if __name__ == "__main__":
  main()