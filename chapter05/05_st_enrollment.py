def enroll_student(*students, min_grade=50, department="Computer Science", **kwargs):
  print(f"Min grade: {min_grade}")
  print(f"Department: {department}")

  print(f"\nEnrolled Students")
  for student in students:
    print(f" - {student}")

  if kwargs:
    print("\nAdditional information:")
    for key, value in kwargs.items():
      print(f"{key.title()} : {value}")
    print("---End of enrollemnt---")
  

def main():
  enroll_student("Chris", "Marinos")
  print("-" * 40)

  enroll_student("Helen", "Nick", "Jack", min_grade=70, academic_year=2026, semester="Fall")

if __name__ == "__main__":
  main()