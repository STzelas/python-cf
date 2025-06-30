# nm -> name mangling
class Point:
  # Αν θέλω να δηλώσω ότι είναι private με χαλαρή προσέγγιση τότε βάζω _count = 0
  # Αν θέλω να δηλώσω ότι είναι private με ΑΥΣΤΗΡΗ προσέγγιση τότε βάζω __count = 0
  __count = 0

  # Αρχικοποιώ σε 0 γιατι δεν μπορώ να δηλώσω
  # πολλούς constructor όπως στην Java. 
  # Δεν υπάρχει overloaded
  def __init__(self, x = 0, y = 0):
    self._x = x  # private
    self.__y = y  # private

  # toString(), χρησιμοποιείται για string representation mode
  def __str__(self):
    return f"({self._x}, {self.__y})"


def main():
  p1 = Point(10, 20)
  print(p1)

  
  print(p1._x) # δεν δουλεύει χωρίς Getter!! είναι __x διπλό underscore private / με ένα δουλευει κανονικά!

  # Στην πραγματικότητα ούτε το __ είναι private
  # Αυτό που κάνει η python λέγεται name mangling. 
  # Αυτό σημαίνει αλλάζει το όνομα της μεταβλιτης!!!
  # πάει και το κάνει __y -> _Point__y
  # print(p1._Point__y) έτσι δουλεύει κανονικά..

  print(p1._x)
  p1.__y = 100
  print(p1.__y)
  # print(p1._Point__y)

  # Μπορώ στην python όταν έχω μια κλάση
  # Δυναμικα ενώ έχω φτιάξει το object
  # Να έρθω και να δημιουργήσω attributes
  p1.sotiris = 1000
  print(p1.sotiris)

  print(p1)



  
if __name__ == "__main__":
  main()
