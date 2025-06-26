# define a tuple of students - tuples() , list[]
# όταν η python βλέπει comma separated values,
# υπονοεί ότι έχουμε πλοιάδα. την φτιάχνει μόνη της
# ακόμα και άν δεν έχει παρενθέσεις
# students = ("Alice", "Bob", "Charlie")
students = "Alice", "Bob", "Charlie" 

print(f"Students: {students}, Type: {type(students)}")

# iterations
for index, student in enumerate(students):
  print(f"{index}: {student}")

print() 
for student in students:
  print(students)

# Γίνεται unpacking η πλειάδα και αντιστοίχηση
first_st, second_st, third_st = students # students[0], students[1], students[3]

print(f"first student: {first_st}")
print(f"second student: {second_st}")
print(f"third student: {third_st}")

# unmodifiable
print(students)
# με μετατροπη σε list γίνεται όμως
students = list(students)
students[0] = "Helen"
students = tuple(students)

print(f"{students}, {type(students)}")