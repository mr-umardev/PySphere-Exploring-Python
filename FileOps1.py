# Define the file path for the source and destination
source_file_path = r'C:\Users\Admin\Desktop\W\W.txt'  # Existing file
destination_file_path = r'C:\Users\Admin\Desktop\W\Y.txt'  # New file

# Writing to the source file (if it doesn't already exist)
with open(source_file_path, 'w') as file:
    file.write("Hello, World!\n")

# Appending to the source file
with open(source_file_path, 'a') as file:
    file.write("Appending this line.\n")

# Copying contents from the source file to the destination file
with open(source_file_path, 'r') as source_file:
    content = source_file.read()  # Read the content

with open(destination_file_path, 'w') as destination_file:
    destination_file.write(content)  # Write the content to the new file

print("Contents copied successfully.")
