# Use a raw string for the file path
file_path = r'C:\Users\Admin\Desktop\W\W.txt'  # For Windows

# Writing to the file
with open(file_path, 'w') as file:
    file.write("Hello, World!\n")

# Appending to the file
with open(file_path, 'a') as file:
    file.write("Appending this line.\n")

# Reading the file content
with open(file_path, 'r') as file:
    content = file.read()
    print(content)




