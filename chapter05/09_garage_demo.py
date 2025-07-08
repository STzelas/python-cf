# FIFO first in first out
from collections import deque

def display_garage(garage: deque) -> None:
  if garage:
    print("Current cars in the garage:")
    for i, car in enumerate(garage, 1):
      print(f"{i}. {car}")
  else:
    print("The garage is empoty")

def add_car_to_garage(garage: deque, max_capacity: int) -> None:
  if len(garage) < max_capacity:
    car_name = input("Enter the name or ID of the car: ")
    if len(car_name) != 7:
      print("---------------")
      print("Invalid car id. It must be 7 characters")
      return
    else:
      garage.append(car_name)
    print(f"{car_name} has entered in the garage.")
  else:
    print("The garage is full. Cannot add more cars.")

def remove_car_from_garage(garage: deque) -> None:
  if garage:
    car_left = garage.popleft() # αφαιρεί το πρώτο
    print(f"{car_left} has left the garage.")
  else:
    print("The garage is empty")

def main():
  garage = deque(["POP1234", "KIO1234", "NPM5432"])
  max_capacity = 20
  
  while True:
    print("---------------")
    print("\nChooce what do you want to do in the Garage: ")
    print("---------------")
    print("1. Add a car")
    print("2. Remove a car")
    print("3. Show the garage")
    print("4. Exit")

    try:
      choice = int(input("Please enter a number between 1 and 5: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
  

    match choice:
      case 1:
        add_car_to_garage(garage, max_capacity)
        display_garage(garage)
      case 2:
        remove_car_from_garage(garage)
        display_garage(garage)
      case 3:
        display_garage(garage)
      case 4:
        print("Exiting...")
        break
      case _:
        print("Invalid input. Please try again.")
    

if __name__ == "__main__":
  main()