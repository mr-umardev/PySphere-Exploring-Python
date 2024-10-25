class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

dog=Dog("Tom")
cat=Cat("Fluff")

dog.speak()
cat.speak()

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Create object of Dog class
dog = Dog()
dog.speak()  # Output: Dog barks

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Mammal:
    def has_hair(self):
        print("Mammals have hair")

class Dog(Animal, Mammal):
    def speak(self):
        print("Dog barks")

# Create object of Dog class
dog = Dog()
dog.speak()  # Output: Dog barks
dog.has_hair()  # Output: Mammals have hair

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def has_hair(self):
        print("Mammals have hair")

class Dog(Mammal):
    def speak(self):
        print("Dog barks")

# Create object of Dog class
dog = Dog()
dog.speak()  # Output: Dog barks
dog.has_hair()  # Output: Mammals have hair

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Create objects of Dog and Cat classes
dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def has_hair(self):
        print("Mammals have hair")

class Bird(Animal):
    def can_fly(self):
        print("Birds can fly")

class Bat(Mammal, Bird):  # Multiple Inheritance
    def speak(self):
        print("Bat squeaks")

# Create object of Bat class
bat = Bat()
bat.speak()  # Output: Bat squeaks
bat.has_hair()  # Output: Mammals have hair
bat.can_fly()  # Output: Birds can fly

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Mammal:
    def has_hair(self):
        print("Mammals have hair")

class Bird:
    def can_fly(self):
        print("Birds can fly")

class Bat(Mammal, Bird):  # Bat inherits from both Mammal and Bird
    def speak(self):
        print("Bat squeaks")

# Creating an object of Bat class
bat = Bat()
bat.speak()  # Output: Bat squeaks
bat.has_hair()  # Output: Mammals have hair
bat.can_fly()  # Output: Birds can fly
