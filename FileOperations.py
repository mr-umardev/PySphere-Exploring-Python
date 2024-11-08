# Use a raw string for the file path
file_path = r'C:\Users\Admin\Desktop\W\T.txt'  # For Windows

with open(file_path, 'r') as file:
    content = file.read()
    print("Contents of the file:")
    print(content)
