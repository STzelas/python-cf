def main():
  store_a_products = {"Apples", "Bananas", "Cherries", "Watermelons"}
  store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

  # Find common products (intersection) available in both stores
  common_products = store_a_products & store_b_products
  print(common_products)

  # Alternative way ( two-way ίδιο πράγμα)
  common_products2 = store_a_products.intersection(store_b_products)
  print(common_products2)

  # Find all unique products (union) accross both stores (A and B)
  all_products = store_a_products | store_b_products
  print(all_products)

  # Using func
  all_products2 = store_a_products.union(store_b_products)
  print(all_products2)

  # Find all products available in store b but not in store a (difference)
  store_b_exclusive = store_b_products - store_a_products
  print(store_b_exclusive)

  # Using func
  store_b_exclusive2 = store_b_products.difference(store_a_products)
  print(store_b_exclusive2)

  # Find products that are in either Store A or Store B but not in both
  unique_to_either_store = store_a_products ^ store_b_products
  print(unique_to_either_store)

  # Using func
  unique_to_either_store2 = store_a_products.symmetric_difference(store_b_products)
  print(unique_to_either_store2)

if __name__ == "__main__":
  main()