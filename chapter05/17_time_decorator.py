# Decorator tutorial, best example
import time

def timer_decorator(func):
  """
  Decorator to measure the execution time of a function.

  Params:
    func (function): The function to be decorated.

  Returns:
    function: The decorated function with added timing functionality.
  """
  def innter_function(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs) # execution
    end_time = time.time()
    print(f"{func.__name__} took {end_time - start_time} seconds to run.")
    return result
  return innter_function

def sum_function(n):
  return sum(range(n))

my_sum_func = timer_decorator(sum_function)
print(my_sum_func(1_000_000))

# Decorators 
# decorate προσθέτει στην function
# επιπλέον functionality αυτής του decorator
# μπορούν να μπουν και παραπάνω απο 1ς decorator
@timer_decorator 
def average_function(n):
  if n == 0:
    return 0
  total_sum = sum(range(n))
  return total_sum / n

print(average_function(100))