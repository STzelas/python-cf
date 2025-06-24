str1 = "Hello, "
str2 = "Coding Factory"

str3 = str1 + str2  # concat
print(str3)

print(str1 * 5)
# Είναι διαφορετικά! Διαφέρουν οι τύποι που έχω αριστερά και δεξιά
# __add__ (αριστερά προς τα δεξιά) , __radd__ (δεξιά προς τα αριστερά)
print(5 * str1) 