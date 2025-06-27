# Βασικό template
def print_cities(*cities): # * αφήνει να βάλει 1 καμία ή περισσότερες τιμές
  if not cities:
    print("No cities provided")
  else:
    print("Cities:", ", ".join(cities))

def main():
  print_cities()
  print_cities("Athens")
  print_cities("Athens", "London", "Paris")

if __name__ == "__main__":
  main()