def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str: # Θα επιστρέφει str
  """
  Returns a string representating a date in the format 'dd/mm/yyyy'

  Args:
    day(int): The day of month. Defaults to 1.
    month(int): The month of the year. Defaults to 1.
    year(int): The year. Defaults to 2000.

  Returns:
    str: The formatted date string.
  """
  return f"{day:02d}/{month:02d}/{year:4d}"  # όταν δεν έχει 2 ψηφία θα βάλει 0 απο μπροστά
  pass

def main():
  print(get_formatted_date())          # 01/01/2000
  print(get_formatted_date(10))        # 10/01/2000
  print(get_formatted_date(14, 2))     # 14/02/2000
  print(get_formatted_date(year=2025)) # 01/01/2025
  print(get_formatted_date(year=2025, day=20, month=10)) 
if __name__ == "__main__":
  main()