num = 10
my_dict = {"count":0}

def main():
  # num += 100 δεν γίνεται / primitive πρέπει να αλλάξει διεύθυνση άρα πρέπει να γίνει νέο variable
  # print(num)
  print(my_dict)
  my_dict["count"] += 1
  print(my_dict)
  pass

if __name__ == "__main__":
  main()