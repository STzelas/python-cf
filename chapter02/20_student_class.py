class Student:
  """
  A class that represents a student with a first name and a last name

  Attrs:
    firstname (str): The first name of the student.
    lastname (str): The last name of the student.
  """
  # Constructor - initialize / self - όπως το this
  def __init__(self, firstname: str, lastname: str): # Το πρώτο όρισμα by convention είναι self! Αλλά μπορεί να είναι οτιδήποτε
    """
    """
    self.firstname = firstname
    self.lastname = lastname


def main():
  st = Student("Bob", "D.") # δεν έχει new, υπονοείται όμως
  print(f"First name: {st.firstname}")
  print(f"Last name: {st.lastname}")

if __name__ == "__main__":
  main()