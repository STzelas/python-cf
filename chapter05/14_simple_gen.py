# yield: convers a simple function into generator
# yield: returns a generator object / ΔΕΝ ΚΑΝΕΙ RETURN

def simple_generator():
  print("First value")
  yield 1
  print("Second value")
  yield 2
  print("Third value")
  yield 3

def main():
  gen = simple_generator()

  print(next(gen)) # εκτελείται μία φορά και μετά περιμένει πότε θα εκτελεστεί ξανά
  print(next(gen))
  print(next(gen))
if __name__ == "__main__":
  main()