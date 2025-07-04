from typing import List, Tuple, Dict, Optional



# args με 2 αστεριακια παραπέμπουν σε λεξικά dict
# kwargs -> κλειδί - τιμή
def get_results(products: List[Tuple[str, int]], **kwargs: Dict[str, str | int]) -> List[Tuple[str, int]]:
  """
  Filters a list of products based on given keyword arguments.
  Each keyword arguments corresponds to a product attribute.

  Params:
    products (List[Tuple[str, int]]): A list of tuples where each tuple contains a brand and a price.
    **kwargs (Dict[str, str | int]): Arbitrary keyword arguments for filtering.

  Returns:
    results (List[Tuple[str, int]]): List of products
  """
  results = [
    (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
  ]
  return results

def main():
  products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
  criteria = {"brand":"lenovo", "price": 100}

  print(get_results(products, **criteria))

if __name__ == "__main__":
  main()
