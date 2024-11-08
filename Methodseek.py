with open('example.txt', 'r') as f:
    f.seek(7)
    print("Current file position after seek:", f.tell())
    print("Data at position 7:", f.read())
