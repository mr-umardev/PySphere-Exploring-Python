print("Umar", "Farooq" , sep="/")
print("Umar"+"Farooq")
a="Umar"
b="Farooq"
# 1. Strings are immutable
original = "Hello"
# Uncommenting the next line will raise an error
# original[0] = 'h'  # This would raise a TypeError

# 2. There is no char type like in C++ or Java
string_example = "Hello"
print(type(string_example))  # Output: <class 'str'> (no separate char type)

# 3. Unicode supported
unicode_string = "Hello, 🌍"  # This includes a Unicode character (Earth emoji)
print(unicode_string)

# 4. + is overloaded to do concatenation
concatenated = "Hello" + " " + "World!"
print(concatenated)  # Output: Hello World!

# 5. Can use single or double quotes, and three double quotes for a multi-line string
single_quoted = 'Single quotes string'
double_quoted = "Double quotes string"
multi_line = """This is a
multi-line string."""
print(single_quoted)
print(double_quoted)
print(multi_line)

# 6. len(String) – returns the number of characters in the String
length = len("Hello")
print(length)  # Output: 5

# 7. str(Object) – returns a String representation of the Object
num = 123
str_num = str(num)
print(str_num)  # Output: '123'
print(type(str_num))  # Output: <class 'str'>

# 8. Strings can be indexed (subscripted)
indexed_string = "Hello"
print(indexed_string[1])  # Output: e

# 9. Index can be negative number
print(indexed_string[-1])  # Output: o (last character)

# 10. Slicing supported
sliced_string = indexed_string[1:4]  # From index 1 to 3
print(sliced_string)  # Output: ell

