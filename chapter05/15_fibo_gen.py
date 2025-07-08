def fibo():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

def main():
  fib = fibo()

  for i in range(11):
    print(f"Fibo({i}) = {next(fib)}")

  fib = fibo()
  for num in fib:
    if num >= 100:
      break
    print(num)
  print("-----------------")
  fib = fibo()
  fib_list = [next(fib) for _ in range(15)]
  print(fib_list)

if __name__ == "__main__":
  main()