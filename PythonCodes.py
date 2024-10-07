#1
def main():
    tup = ('Bengaluru', 33, '17/03/2015:13:40')
    print(tup)
    # immutable
    # tup[1] = 36  # This line is commented out to avoid error
    tup = (tup[0], 36, tup[2])
    print(tup)
    # slicing
    tup2 = tup[0:2]
    print(tup2)
    # nesting
    tup3 = ('Bengaluru', (33, '17/03/2015:13:40'))
    print(tup3)

if __name__ == '__main__':
    main()
#2
def main():
    var1 = 25
    var2 = var1
    var2 += 5
    print(var1, var2)  # Added parentheses for print
    print(type(var1))

if __name__ == '__main__':  # Fixed the condition
    main()
#3
def main():
    my_str = '0123456789'
    print(my_str, len(my_str), '\n')

    # Index +ve
    index = 2
    print("my_str[%d] => %s" % (index, my_str[index]))

    # Index -ve
    index = -1
    print("my_str[%d] => %s" % (index, my_str[index]))

    # Slicing
    print("---slicing---")
    substr = my_str[1:7]
    print('my_str[1:7] => ' + substr)

if __name__ == '__main__':
    main()
#4
def main():
    val1 = 20.5E2  # This is scientific notation for 2050.0
    val2 = int(val1)  # Convert float to integer
    print(val1, val2)  # Print both values

    # -------------------------
    val3 = 30
    val4 = float(val3)  # Convert integer to float
    print(val3, val4)  # Print both values

    # -------------------------
    comp1 = 5 + 2j  # Create a complex number
    comp1 += 3  # Add a real number
    print(comp1)  # Print the updated complex number
    comp1 += 6j  # Add an imaginary number
    print(comp1)  # Print the final complex number

if __name__ == '__main__':  # Fixed the condition
    main()
#5
def main():
    weather = ['Bengaluru', 33, '17/03/2015:13:40']
    print(weather)  # Print the original list

    # List is mutable
    weather[1] = 36  # Modify the second element
    weather.append("@Jaynagar")  # Append a new element to the list

    # List slicing
    print(weather[1:])  # Print the list from the second element onward

    # Stack operations
    item = weather.pop()  # Remove and return the last item
    print(weather, item)  # Print the modified list and the popped item

    weather.append('@Rajajinagar')  # Append another item

if __name__ == '__main__':  # Fixed the condition
    main()
#6
def main():
    weather = {
        'Bengaluru': (33, '18/02/2015'),
        'Delhi': (43, '18/02/2015'),
        'Mumbai': (40, '18/02/2015')
    }

    # Accessing data
    city = weather['Bengaluru']
    print(city)  # Print the temperature and date for Bengaluru

    # Mutable dictionary
    weather['Hyderabad'] = (40, '18/02/2015')  # Add a new city
    print(weather)  # Print the updated dictionary

    # Important operations
    print(weather.keys())  # Print all keys (cities) in the dictionary
    city_info = weather.pop('Bengaluru')  # Remove and return the entry for Bengaluru
    print(weather.keys())  # Print the keys after removing Bengaluru

if __name__ == '__main__':  # Fixed the condition
    main()
#7
def max_func(x, y):
    if x < y:
        return y
    else:
        return x

def min_func(x, y):
    if x < y:
        return x
    else:
        return y

def myfunc(alg1, alg2):
    print(alg1(8, 9))  # Call the first function and print its result
    print(alg2(8, 9))  # Call the second function and print its result

def main():
    Max = max_func  # Assign the max function to Max
    print(Max)  # Print the function reference
    print(type(Max))  # Print the type of Max
    myfunc(Max, min_func)  # Call myfunc with Max and min_func

if __name__ == '__main__':  # Fixed the condition
    main()
#8
class ListDemo:
    def __init__(self, initList):  # Corrected constructor method
        self._list = initList

    def ListDemo1(self):
        myList = self._list
        myList.append("Text data")
        myList.append(4)
        print("List Items:")
        self.Show()

    def ToUpper(self):
        newList = []
        for index in self._list[:]:
            eachItem = index

            print("eachItem:", eachItem)
            if isinstance(eachItem, str):  # Check if eachItem is a string
                eachItem = eachItem.upper()
            newList.append(eachItem)
        self._list = newList

    def ListDemo2(self):
        myList = ["text1", 55, 88.2, -27]
        print("List Items:")
        self.Show()

    def Show(self):
        print(self._list)

    def __str__(self):  # Corrected __str__ method
        return 'ListDemo class'


# Inheritance
class Names(ListDemo):
    def __init__(self, initList):  # Corrected constructor method
        super().__init__(initList)  # Call the parent class constructor


if __name__ == '__main__':  # Corrected the condition
    demo = ListDemo(["text1", 55, 88.2, -27])
    demo.ToUpper()
    demo.Show()
    demo.ListDemo1()
    print(demo)

    kk = Names(['aaa', 'bbb'])
    kk.Show()


def main():
    s = '0123456789'  # Changed variable name from str to s to avoid conflict with built-in str
    print(s, len(s), '\n')  # Print the string and its length

    # Attempting to modify a string directly will raise an error
    # str[1] = '3'  # This line is commented out because strings are immutable

    # Indexing (positive)
    index = 2
    print("s[%d] => %s" % (index, s[index]))

    # Indexing (negative)
    index = -1
    print("s[%d] => %s" % (index, s[index]))

    # Slicing
    print("---slicing---")
    substr = s[1:7]
    print('s[1:7] => ' + substr)
    substr = s[:7]
    print('s[:7] => ' + substr)
    substr = s[1:]
    print('s[1:] => ' + substr)
    substr = s[3:-3]
    print('s[3:-3] => ' + substr)

    # Unicode string
    text = u'unicode string'
    # Various string functions
    print(dir(text))


if __name__ == '__main__':  # Fixed the condition
    main()





