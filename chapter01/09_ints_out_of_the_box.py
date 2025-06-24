a = 10
b = 20

result = a + b

print(f"{a} + {b} = {result}")

print("------------------")

print("Type of a:", type(a))
print(f"Type of a: {type(a)}")

# __add__ special (magic) methods που υπάρχουν
# όταν έχουμε τους ίδιους τύπους
# result = a + b αυτό το + στην ουσία
# είναι το παρακάτω ακριβώς. γίνεται
# υπερφόρτωση του τελεστή +
# γίνεται και με str επειδη υπερφορτώνεται
# τόσο σε ακαιρέους όσο και str
# τότε κάνει concat
magic_result = a.__add__(b)

print(f"Magic result: {magic_result}")