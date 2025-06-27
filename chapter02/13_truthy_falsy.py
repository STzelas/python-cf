# Falsy - Truthy values
# Falsy: 0, 0.0, 0j, "", [], (), {}, set(), False, None # Αν θέλω να αρχικοποιήσω σύνολο, χρησιμοποιώ constructor ή set()


empty_dict = {}
print(type(empty_dict))

a = 5

if a > 0 and a < 10:
  print("Valid number")

if 0 < a < 10:
  print("Valid number 2")

