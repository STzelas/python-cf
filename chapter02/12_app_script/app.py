# import my_calculations
# import μόνο την function που ήθελα
# και όχι όλο το module που πχ αν είχε
# παρα πολλές methods που δεν τις ήθελα
# θα ήταν ανούσιο και inefficient
from my_calculations import my_add_function 

num2 = 10

# res = my_calculation.my_add_function(200, 300)
res = my_add_function(100, 200)
print(res) # result 300