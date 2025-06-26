# import my_calculations
# import μόνο την function που ήθελα
# και όχι όλο το module που πχ αν είχε
# παρα πολλές methods που δεν τις ήθελα
# θα ήταν ανούσιο και inefficient
from my_calculations import my_add_function as my_add, num1

num2 = 10

# res = my_calculation.my_add_function(200, 300)
res = my_add(num1, num2)
print(res) # result 300