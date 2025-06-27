choice = 'q'


if choice == 'q' or choice == "Q":
  print("Quit")
else:
  print("Continue")

print("-----------")

if choice.lower() == 'q':
  print("Quit")
else:
  print("Continue")

print(f"{"Quit" if choice == 'q' or 'Q' else 'Continue'}")

if choice in ('q', 'Q'):
  print("Quit")
else:
  print(("Continue"))