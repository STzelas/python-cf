def upscale_grades(grades):
  return [grade + 1 if grade <= 9 else grade for grade in grades]

def filter_passed(grades):
  return [grade for grade in grades if grade >= 5]

def categorize_grades(grades):
  passed = [grade for grade in grades if grade >= 5 and grade <= 10]
  failed = [grade for grade in grades if grade < 5]
  honors = [grade for grade in grades if grade == 10]

  return passed, failed, honors

def calculate_average(grades):
  return sum(grades) / len(grades) if grades else 0

def main():
  grades = [7, 5, 9, 10, 5, 3, 7, 2, 8, 0]

  upscaled_grades = upscale_grades(grades)
  print(f"Initial grades: {grades}")
  print(f"Upscaled grades: {upscaled_grades}")

  passed_gd, failed_gd, honored_gd = categorize_grades(grades=grades)

  print(f"Passed Students: {passed_gd}")
  print(f"Failed Students: {failed_gd}")
  print(f"Honored Students: {honored_gd}")
  


if __name__ == "__main__":
  main()