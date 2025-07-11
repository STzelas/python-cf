def main():
  students = {
  'Alice': 85,
  'Bob': 90,
  'Charlie': 94,
  'Diana': 80,
  'Eve': 81
  }
  
  # Find the student with the student name lowest alphabetic order
  student_with_min_alphabet_name = min(students)
  print(f"Student with the lowest alphabetical order: {student_with_min_alphabet_name}")

  # Student with min grade
  student_with_min_grade = min(students, key=students.get) # δεν καλώ την get αλλα του λέω θα εφαρμώσεις ως get την fucntion get πάνω στο students και τα αποτελεσματα θα τα filtrareis και θα φερεις το min
  print(f"Student with the lowest grade: {student_with_min_grade}")

  # Student with the shortest name by length
  student_with_shortest_name = min(students, key=len)
  print(f"Student with the lowest name length: {student_with_shortest_name}")

if __name__ == "__main__":
  main()