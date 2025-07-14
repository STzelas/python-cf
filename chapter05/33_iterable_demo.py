class DataCollection:
  def __init__(self, data):
    self.data = data

  def __iter__(self):
    return iter(self.data)
  
  def __getitem__(self, index):
    return self.data[index]
  
  # Άλλη η υλοποίηση εδώ και άλλη η υπερφόρτωση της len για κάτι άλλο
  def __len__(self):
    return len(self.data)
  
  def __repr__(self):
    return f"DataCollection({self.data})"
  
def main():
  collection = DataCollection([1, 2, 3, 4, 5])

  print(f"DataCollection: {collection}")  # δίνει την εκτύπωση της __repr__

  # Iterate
  for item in collection:  # iter στο collection
    print(item)

  # Unpacking 
  a, b, c, d, e = collection
  print(a, c)

  # indexing
  print(f"Element at index 0: {collection[0]}")   # __getitem__
  print(f"Element at last index: {collection[-1]}")   # __getitem__

  # slicing
  print(collection[1:4])

  # len
  print(f"Length of collection: {len(collection)}")


if __name__ == "__main__":
  main()