# pos_args -> positional arguments / πρέπει να τα optional να είναι μετά τα positional
# Αν έχουμε τιμή στα πρώτα args πρέπει όλα να έχουν
# *args -> αφού τελείωσουν τα υπόλοιπα, μπορώ να βάλω ένα σύνολο τιμών απευθείας
# (όπως στην rpint που έχει τιμή,)
# μετά μπορώ να βάλω **kwargs -> μου δίνει την δυνατότηα να βάλω key-value(σαν dict) pairs (ΌΤΙ ΘΈΛΩ)
def test_args_func(pos_arg1: any, pos_arg2: any, opt_arg1=None, opt_arg2=None, *args, **kwargs):
  """
  Function to demonstrate the usage of positional, optional, additional optional(*args) 
  and additional keyword arguments (**kwargs)

  Parameters:
    pos_args1 (Any): The first positional argument.
    pos_args2 (Any): The second positional argument.
    opt_arg1: The first optional argument. Defaults to none
    opt_arg1: The second optional argument. Defaults to none
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.
  """
  # Print positional arguments
  print("Pos arg1:", pos_arg1)
  print("Pos arg2:", pos_arg2)

  # Print optional arguments
  print("Opt arg1:", opt_arg1)
  print("Opt arg2:", opt_arg2)

  # Print additional pos args
  if args:
    print("Additional pos args")
    for arg in args:
      print(arg)
  
  if kwargs:
    print("Additional keyword args")
    for key, value in kwargs.items(): # επιστρέφονται πλοιάδες που γίνονται unpacking
      print(f"{key}:{value}")

def main():
  test_args_func("Hello", "CF7", 100, 200)
  print("--------------1--------------")

  test_args_func("Hello", "CF7", opt_arg2 = 100)
  print("--------------2--------------")
  test_args_func("Hello", "CF7", name = "Sotiris", age = 26)

  print("--------------3--------------")
  test_args_func("Hello", "CF", # pos_arg1, pos_arg2
                 100, 200, # opt_arg1, opt_arg2
                 300, "Sotiris", # *args
                 name = "Sotiris", steet = "Coding"
  )

if __name__ == "__main__":
  main()