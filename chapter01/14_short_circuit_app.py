username = input("Please enter your username: ")

email = input("Please enter your email: ")

valid_user = username or "User"

'''
if email:
  print(f"Hello {valid_user}, your email is: {valid_email}")
else:
  print(f"Hello {valid_user}, please provide you email.")
'''
# Αν υπάρχει email εντός τις παρένθεσης έχουμε truthy && data οπότε εμφανίζει τα data
# Αν δεν υπάρχει τότε είναι falsy και πάει στην επόμενη παράσταση (ενα str) το 
# οποιο και επιστρέφει
print(f"Hello {valid_user}, " + ((email and f"your email is: {email}") or ("please provide your email"))) 

