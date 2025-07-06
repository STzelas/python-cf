cities = ["london", "paris", "athens", "barcelona"]

# map built-in function παίρνει ως όρισμα
# μία συνάρτηση και 1 iterable object
# σε κάθε iteration εφαρμοζει την συνάρτηση
cap_cities = list(map(lambda city: city.title(), cities))
print(f"Cap cities: {cap_cities}") # Τα έκανε title (έκανε κεφαλαιο το 1ο γράμμα)