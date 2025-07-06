from functools import reduce

# list of nums(int)
my_ints = [1, 2, 3, 4, 5]

# θέλω να επιστρέψω το άθροισμα τους (όχι με sum)
# βάζουμε lambda κάνει μια πραξη και επιστρέφει το αποτελεσμα
# και μετά ξανά και ξανά μέχρι να τελειώσει -> επιστρέφει ένα result
result = reduce(lambda x, y: x + y, my_ints) # 1 + 2 -> 3 + 3 -> 6 + 4 -> 10 + 5
print(result)

# το ίδιο και εδώ αλλά με πολλαπλασιασμό
result2 = reduce(lambda x, y: x * y, my_ints)
print(result2) 