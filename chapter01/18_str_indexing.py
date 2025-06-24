message = "Coding Factory"

# str λειτουργεί και εδώ σαν array / immutable primitive type
# 0 index ξεκινάει από το 0, 
print("Result:", message[0]) # result: C
print("Result:", message[1]) # result: o
print("Result:", message[2]) # result: d
print("Result:", message[3]) # result: i
print("Result:", message[4]) # result: n
print("Result:", message[5]) # result: g

'''
  message[0] = 'c' # Δεν γίνεται αυτό
'''

# εδώ αλλάζει το reference, 
# ενώ πάνω πάμε να κάνουμε modify το string.
# message = "New message" 
# print(message)

# len είναι built-in function
# παίρνει ένα οποιοδήποτε διασχήσιμο object
# και μας δείχνει πόσα στοιχεία είναι (obj: Sized)
print(f"Length of {message} = {len(message)}")

# for
for char in message:
  print(char, end=" ")
print()

# Python - Η for δεν έχει int i = 0; κλπ
# χρησιμοποιούμε την range που επιστρέφει
# κάθε φορά το στοιχείο όταν αυτό ζητείται

for i in range(10 + 1):  # range(start = 0, stop = 10, step = default 1)
  print(i)

print("-" * 10)

# το i υπάρχει και μετα / έξω απο την for.
# Στην python η for ΔΕΝ ΈΧΕΙ SCOPE!!
print(i) 

for i in range(len(message)):
  print(message[i], sep= "")

# result 1ου και τελευταιου στοιχειου πρόσθεση
# result = 
my_num = 123456789
str_num = str(my_num)
first_num = int(str_num[0])

# for i in range(len(str_num)):
#   print()
# last_num = int(str_num[i])

last_num = int(str_num[-1])
print(first_num + last_num)
print(f"Result = {int(str_num[0]) + int(str_num[-1])}")




