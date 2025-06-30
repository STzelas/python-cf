import math

class Point:
  """
  A class representing a point in 2D space.

  Attributes:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.
  """

  def __init__(self, x: float = 0, y: float = 0):
    """
    Initialize a Point object with specified x and y coordinates

    Args:
      x (float): The x-coordinate of the point. Defaults to 0.
      y (float): The y-coordinate of the point. Defaults to 0.
    """
    self.x = x
    self.y = y

  # __str__ είναι σαν την toString() στην java
  # Αν δεν υπάρχει αυτή η μέθοδος τότε όταν
  # θα χρειαστεί να κάνω print θα εμφανίζει 
  # ενα σημείο στην μνήμη

  # p1 = Point(10, 20)
  # p2 = Point(30, 40)

  # print(f"{p1}")
  # print(f"{p2}")
  # print(f"Distance: {p1.distance_to(p2):.3f}")

  # Result:
  # <__main__.Point object at 0x00000216025E6A50>
  # <__main__.Point object at 0x0000021602868A50>
  # Distance: 28.284
  def __str__(self):
    return f"({self.x}, {self.y})"
  
  def distance_to(self, other):
    return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
  
def main():
  p1 = Point(10, 20) # εννοείται new
  p2 = Point(30, 40) # εννοείται new

  print(f"{p1}")
  print(f"{p2}")

  print(f"Distance: {p1.distance_to(p2):.3f}")

if __name__ == "__main__":
  main()