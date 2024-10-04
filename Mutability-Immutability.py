"""tuple2=(0,1,2,3)
tuple2[3]=4
print(tuple2)"""

dictionary={"name":"umar","age":"20","USN":"1BM22IS116","Course":"Information Science and Engineering"}
print(dictionary)
dictionary_change=dictionary
dictionary_change["Course"]="Computer Science and Engineering"
print(dictionary_change)

first_set = {1, 2, 3}
print(first_set)
updated_set = first_set
first_set.add(4)
print(updated_set)

first_list = [4,5,6]
first_list.append(7)
print(first_list)

first_list.insert(1, 8)
print(first_list)

first_list.remove(5)
print(first_list)

popped_element = first_list.pop(0)
print(first_list)
print(popped_element)


"""def fun():
    a=10
    print(a)

fun()

def fun():
    a=15
    print(a)
fun()"""

"""def my_function():
    return "Hello, World!"

# Calling the function
print(my_function())

try:
    my_function() = lambda: "New Function!"
except SyntaxError as e:
    print(f"Error: {e}")"""


class ImmutablePoint:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

# Create an instance
point = ImmutablePoint(2, 3)
print(point.x)  # Output: 2
print(point.y)  # Output: 3


try:
    point.x = 5
except AttributeError as e:
    print(f"Error: {e}")



