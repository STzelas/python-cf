import math

name = "Alice"
age = 20

print("CF7")
print("PI:", math.pi)

print(name, "is", age, "years old")


print("--------String Concatenation--------")

# print(name + "is " + age + " years old") δεν κάνει αυτόματα typecast σε string οπως στην java

print(name + " is " + str(age) + " years old")

# Python2 style
print()
print("Python2 Style")
print("PI = %6.2f" %math.pi)
print("%s is %d years old" %(name, age))  # σαν την printf περίπου

# Python3 style
print("\nPython3 Style")
print("Alice is {0:2d}".format(age),"years old")
print("PI is {0:.3f}".format(math.pi))

print("PI = {0:.3f} and age = {1}".format(math.pi, age))  # το 0 και 1 συμβολίζει ποιο απο τα δυο μέσα στην format

print("{0} is {1} years old".format(name, age), end="***") #small task

# f strings
print(f"\n{name} is {age} years old") # αυτό ονομάζετα f string μοιάζει με interpolation