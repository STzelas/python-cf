class FactoIterator:
  def __init__(self, n):
    if n < 0:
      raise ValueError("Factorial is not defined for negative numbers.")
    self.n = n
    self.result = 1
    self.order = 1

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.order > self.n:
      raise StopIteration
    
    self.result *= self.order
    self.order += 1
    return self.result
  
def main():
  facto_iter = FactoIterator(10)

  # get the first factorial using next function

  a = next(facto_iter)
  print(a)

  for facto in facto_iter:
    print(facto)

  new_facto_iter = FactoIterator(5)

  for index, factorial in enumerate(new_facto_iter, start=1):
    print(f"Factorial of {index} = {factorial}")

if __name__ == "__main__":
  main()