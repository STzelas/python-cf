def main():
  grades = [7, 5, 9, 10, 5]

  upscale_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
  print(f"Upscaled grades: {upscale_grades}")

  # using map()
  upscale_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
  print(f"Upscaled grades using map(): {upscale_grades2}")

  # list compr
  passed_grades = [grade for grade in grades if grade >= 5]
  print(f"Passed grades using list compr: {passed_grades}")

  # filter
  passed_grades2 = list(filter(lambda grade: grade >= 5, grades))
  print(f"Passed grades using filter(): {passed_grades2}")
  

if __name__ == "__main__":
  main()