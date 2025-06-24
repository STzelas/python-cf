name = "Bob"

print("-----------or----------")

# To none δεν είναι True, False, είναι ομως Falsy, or "User"
# άρα επιστρέφει User.
valid_user = None or "User"

print(f"Hello {valid_user}")


print("-" * 20)

# Truthy or Truthy, σταματάει στο 1ο.
# Αν το str ήταν "" κενό (άρα Falsy)
# τότε θα επέστρεφε User
valid_user = name or "User" 
print("Hello", valid_user)

print("-----------and----------")

email = "example@mail.com"

valid_email = email and email != ""
print("Valid email:", valid_email) # Valid email: True

if valid_email:
  print(f"Hello {valid_user}, your email is: {valid_email}")
else:
  print(f"Hello {valid_user}, please prodivde you email.") 