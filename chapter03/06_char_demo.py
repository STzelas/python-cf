def process_characters() -> None:
  """
  Returns the ordinal value of a char.
  """
  ch = input("Please insert a char: ")

  # Αναγκαστικά πρέπει να χρησιμοποιήσω while
  # Δεν έχουμε do while
  while ch != '#':
    print(ch, ":", ord(ch))
    ch = input("Please insert a char: ")
  print("Goodbye")

def main():
  process_characters()


if __name__ == "__main__":
  main()