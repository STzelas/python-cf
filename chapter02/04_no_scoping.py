import random

random_numbers = []

for i_ in range(10):  # όταν το i δεν το χρησιμοποιώ γράφω i_ / βάζει δηλαδή placeholder
  num = random.randint(1, 100) # random int / included και οι δυο αριθμοι απο 1 εως 100
  random_numbers.append(num)
  
print(random_numbers)

for num in random_numbers:
  if(num % 2 == 0):
    even = num
  
print(even)