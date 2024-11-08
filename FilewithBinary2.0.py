# Writing new binary data using 'w+'
with open('I.bin', 'w+b') as file:
    file.write(bytes([10, 20, 30, 40, 50]))  # Initial data
    file.seek(0)
    print("After 'w+':", file.read())

# Appending new binary data using 'a+'
with open('I.bin', 'a+b') as file:
    file.write(bytes([60, 70, 80]))  # Data to append
    file.seek(0)
    print("After 'a+':", file.read())

# Reading and modifying data using 'r+'
with open('I.bin', 'r+b') as file:
    file.seek(0)  # Move to the start
    file.write(bytes([255]))  # Modify first byte
    file.seek(0)
    print("After 'r+':", file.read())
