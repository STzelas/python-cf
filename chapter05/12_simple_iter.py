class SimpleIterator:
  def __init__(self, data):
    self.data = data
    self.index = 0

  # magic method, Κάνω return το ίδιο το object
  def __iter__(self):
    return self
  
  # στην java έχουμε hasNext(), εδώ υλοποιώ την __next__
  def __next__(self):
    if self.index < len(self.data):
      result = self.data[self.index]
      self.index += 1
      return result
    else:
      raise StopIteration
    
def main():
  numbers = [10, 20, 30, 40, 50]

  my_iter = SimpleIterator(numbers)

  a = next(my_iter) # κάνει consume το 1ο στοιχείο
  print(a)          # υπάρχει όμως (το βάζω στο a πχ)
  print("------")
  for item in my_iter:
    print(f"item: {item}")

if __name__ == "__main__":
  main()