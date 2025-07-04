
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums = list(range(1, 11))
print(nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even numbers

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(type(even_numbers)) # είναι iterator το class filter

for num in even_numbers:
  print(num, end=" ")
print()
print("--------------")
# Δεν εκτυπώνεται δεύτερη φορά
# είναι iterator, καταναλώθηκε
# δεν υπάρχει άλλο εδώ
for num in even_numbers:
  print(num, end=" ")
print()

print(*even_numbers)

# list

even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_list)
print(even_numbers_list)

def even_num_func(n):
  return n % 2 == 0

my_list = list(filter(even_num_func, numbers))
print(my_list)