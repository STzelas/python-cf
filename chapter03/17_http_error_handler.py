# Πριν την 3.10 δεν είχαν match

def get_http_error(error_code: int):
  error_messages = {
    200: "OK",
    400: "Bad Request",
    404: "Not found"
  }
  return error_messages.get(error_code, "Unknown Error")

def main():
  error_code = 404
  print(get_http_error(error_code))

if __name__ == "__main__":
  main()