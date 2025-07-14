import os

def read_file(file_path: str):
  """
  Reads and prints the content of a file along with additional details.

  Parameters:
  file_path (str): The path to the file to be read.
  """
  if not os.path.isfile(file_path):
    print(f"Error: {file_path} does not exists")
    return
  
  try:
    with open(file_path, "r") as f:
      # Display file metadata
      print(f"Filename: {f.name}")
      print(f"Closed: {f.closed}")
      print(f"Opening mode: {f.mode}")

      contents = f.read()
      print(f"Contents: {contents}")

  except FileNotFoundError as e:
    print(f"Error: {file_path} not found: {e}")
  except IOError as e:
    print(f"Error reading file {file_path}: {e}")
  
  print(f"File closed after with-block: {f.closed}")

def read_file_contents(file_path: str):
  """
  Reads the content of a file and returns it.

  Parameters:
  file_path (str): The path to the file to be read.

  Returns:
  str: The content of the file.
  """
  if not os.path.isfile(file_path):
    print(f"Error: {file_path} does not exists")
    return None
  
  try:
    with open(file_path, "r") as f:
      return f.read()
  except FileNotFoundError as e:
    print(f"Error: {file_path} not found: {e}")
  except IOError as e:
    print(f"Error reading file {file_path}: {e}")
  return None

def create_file(file_path:str, content:str):
  """
  Creates a new file with the given content.

  Parameters:
  file_path (str): The path to the file to be created.
  content (str): The content to write to the file.
  """
  try:
    with open(file_path, "w") as f:
      f.write(content)
      print(f"File {file_path} created!")
  except IOError as e:
    print(f"Error creating file {file_path} : {e}")
  
def update_file(file_path:str, content:str):
  """
  Updates the content of an existing file by appending new content.

  Parameters:
  file_path (str): The path to the file to be updated.
  content (str): The content to append to the file.
  """
  if not os.path.isfile(file_path):
    print(f"Error: {file_path} does not exists")
    return None

  try:
    with open(file_path, "a") as f: # "a" append
      f.write(content)
      print(f"File {file_path} with new content.")
  except IOError as e:
    print(f"Error creating file {file_path} : {e}")

def delete_file(file_path:str):
  """
  Deletes the specified file.

  Parameters:
  file_path (str): The path to the file to be deleted.
  """
  if not os.path.isfile(file_path):
    print(f"Error: {file_path} does not exists")
    return None
  
  try:
    os.remove(file_path)
    print(f"File {file_path} removed.")
  except IOError as e:
    print(f"Error creating file {file_path} : {e}")

def main():
  """
  Main function to perform CRUD operations on files.
  """
  # Creating a new file
  print("Creating 'example.txt':")
  create_file('example.txt', "This is the initial content of the file.\n")
  print()

  # Reading and printing details and contents of the created file
  print("Reading 'example.txt':")
  read_file('example.txt')
  print()

  # Updating the file by appending new content
  print("Updating 'example.txt':")
  update_file('example.txt', "This is the appended content.\n")
  print()

  # Reading and printing updated contents of the file
  print("Reading updated 'example.txt':")
  read_file('example.txt')
  print()

  # Deleting the file
  print("Deleting 'example.txt':")
  delete_file('example.txt')
  print()

  # Attempting to read the deleted file
  print("Reading 'example.txt' after deletion:")
  read_file('example.txt')
  print()

if __name__ == "__main__":
  main()