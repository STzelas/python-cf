name = input("Please insert your name: ")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height: "))

is_student = input("Are you student? (Yes/No): ").lower() == "yes"   # .lower() lower case

print(f"Hello {name}")

# 1 tab αντί για {} στην python
# Δεν θέλει is_student == true οπως java, είναι όπως Js
if is_student:
  print("You are student")
  print("...")
else:
  print("You are not student")

# Python3 Style
print("Your age is {} and your height is {:.2f} meters".format(age, height))
