# Initial binary data to write
initial_data = bytes([120, 3, 255, 0, 100])  # Data to write

# Writing binary data to the file using 'wb'
with open('I.bin', 'wb') as file:
    file.write(initial_data)

# Reading the binary data from the file using 'rb'
with open('I.bin', 'rb') as file:
    data = file.read()

# Display the contents after writing
print("After 'wb':")
print("Binary Data:", data)
print("Byte Values:", list(data))

# Sample binary data to append
data_to_append = bytes([101, 102, 103])  # Data to append

# Appending binary data to the file using 'ab'
with open('I.bin', 'ab') as file:
    file.write(data_to_append)

# Reading the binary data again to display updated contents
with open('I.bin', 'rb') as file:
    updated_data = file.read()

# Display the updated contents after appending
print("\nAfter 'ab':")
print("Binary Data:", updated_data)
print("Byte Values:", list(updated_data))
