# Ακολουθία fibonacci αποτελείται απο τους αριθμούς 0 - 1, το επόμενο στοιχείο
# είναι το άθροισμα των τελευταίων 2 στοιχείων, άρα  0 - 1 - 2 - 3 - 5 - 8

def main():
  n = int(input("Please insert an integer: "))

  a = 0
  b = 1

  for i in range(2, n + 1):
    temp = a # το αποθηκεύω σε μία προσωρινή μεταβλιτή
    a = b
    b = temp + b
  print(f"The {n} Fibo number is {b}")

if __name__ == "__main__":
  main()