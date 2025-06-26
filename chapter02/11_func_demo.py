
def say_hello(name:str = "Coding Factory"):  # def = definition έτσι δηλώνουμε methods | το str δεν είναι τύπος. είναι annotation
  """
  Print a greeting message.

  Args:
    name(str): The name to greet. Default value 'Coding Factory'
  """
  # pass # placeholder για να μην έχω errors
  print(f"Hello {name}")

# main δική μας καλή προσεγγιση
def main():
  # say_hello(10)  # 10
  say_hello()
  say_hello("Panos")
  
  # print(say_hello.__doc__) # εκτυπώνει το documentation της συναρτησης
  help(say_hello)            # εκτυπώνει το documentation της συναρτησης
  pass

# Εκτυπώθηκε Hello επειδή κάλεσα main που κάλεσε την say_hello
# Ειδική μεταβλιτή __name__ . Παίρνει σαν όνομα την main επειδή εδώ καλώ την main
# Αν δεν ήταν η main μέσα εδώ τότε θα λεγόταν όπως λέγεται το module
# δηλαδή 11_func_demo
if __name__ == "__main__":
  main()

