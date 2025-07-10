import logging

def main():
  log_file = 'cf7.log'

  # This is our file handler
  file_handler = logging.FileHandler(log_file, mode='a')

  # Create a list of handler for the logger
  handlers = [file_handler]

  # our logger
  logger = logging.getLogger('logging_app')

  logging.basicConfig(
    handlers=handlers,
    level=logging.INFO, # Logging Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
  )

  my_nums = [10, 20, 30, 40, 50]
  
  num_to_find = 2.3

  try:
    index = my_nums.index(num_to_find)
    print('Found')
    print(index)
  except ValueError as e:
    logger.error(f"Error occured: {e}", exc_info=True)

if __name__ == "__main__":
  main()