def main():
  nums = (1, 2, 3, 4, 5) # tuple
  print(f"Type of nums: {type(nums)}")

  mixed_tuple = (1, 2, [3, "CF7"], "Hello")

  try:
    nums[0] = 100 # Δεν γίνεται -> δεν μπορούμε να αλλάξουμε primitive στο tuple γιατι δεν αλλάζει η διευθυνση μνήμης
  except TypeError as e:
    print(f"Error: {e}")

  mixed_tuple[2][0] = 300  # γίνεται. Η διεύθυνση μνήμης της λίστας εντός του tuple, παραμένει ίδια, αλλάζει το εσωτερικό της (που είναι modifiable)
  print(mixed_tuple)

if __name__ == "__main__":
  main()