my_list = [1, 2, 3, 4, 5]

new_list = [1, 2, 3]
def main():
  
  # simple unpacking
  a, b, c, d, e = my_list  # αντιστοιχεί
  print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, ")

  # skipping some values
  a, _, c, _, e = my_list  # αντιστοιχεί
  print(f"a = {a}, c = {c}, e = {e}, ")

  # unpack the first element and then the rest
  a, *b = my_list  # με * θα μπουν όλα εκεί (μιά λίστα απο 4 αριθμούς αρα)
  print(f"a = {a}, b = {b}")

  *a, b = my_list
  # θα πάρει το τελευταίο το b και τα υπόλοιπα θα μπουν στο a
  print(f"a = {a}, b = {b}")

  *a, b, c = my_list
  print(f"a = {a}, b = {b}, c = {c}")

  
  first, *middle, last = my_list
  print(f"first element = {first}, middle element(s) = {middle}, last element = {last}")

  # Με αστεράκι το 2ο element (γιατί τώρα είναι μονο 3, θα είναι λίστα με 1 στοιχείο)
  first, *middle, last = new_list
  print(f"first element = {first}, middle element(s) = {middle}, last element = {last}")

if __name__ == "__main__":
  main()

