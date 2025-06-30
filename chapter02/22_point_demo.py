class Point:
  # Αν θέλω να δηλώσω ότι είναι private με χαλαρή προσέγγιση τότε βάζω _count = 0
  # Αν θέλω να δηλώσω ότι είναι private με ΑΥΣΤΗΡΗ προσέγγιση τότε βάζω __count = 0
  __count = 0

  # Αρχικοποιώ σε 0 γιατι δεν μπορώ να δηλώσω
  # πολλούς constructor όπως στην Java. 
  # Δεν υπάρχει overloaded
  def __init__(self, x = 0, y = 0):
    self.__x = x  # private
    self.__y = y  # private
    Point.__count += 1

  # toString(), χρησιμοποιείται για string representation mode
  def __str__(self):
    return f"({self.__x}, {self.__y})"

  # magic method repr , χρησιμοποιείται για debugging mode
  def __repr__(self):
    return f"Point(x={self.__x}, y={self.__y})"
    
  # Να συγκρίνω ένα object με ένα άλλο object
  def __eq__(self, other):
    # παίρνει ένα object και ένα class, επιστρέφει bool,
    # True άν το Object είναι Instance της class
    if isinstance(other, Point):
      return self.__x == other.__x and self.__y == other.__y
    else:
      return False 
      
  # def __lt__, __gt__

  # cls by convention παραπέμπει σε class
  @classmethod
  def get_count(cls):
    return cls.__count

  # Πως δηλώνουμε τα properties
  # Πάντα πρώτα Getter και μετά Setter

  @property # getter / ότι όνομα έχει η μεταβλητή έχει και η function
  def x(self):
    return self.__x

  @x.setter # setter / decorators, property για getter, .setter για setters
  def x(self, x):
    self.__x = x

  @property
  def y(self):
    return self.__y

  @y.setter
  def y(self, y):
    self.__y = y

def main():
  p1 = Point(10, 20)
  p2 = Point(11, 20)

  
  print(p1)
  print(p2)
  p1.x = 10
  print(p1.x, p1.y)
  print(f"p1 == p2: {p1 == p2}")

  print(Point.get_count())


if __name__ == "__main__":
  main()
