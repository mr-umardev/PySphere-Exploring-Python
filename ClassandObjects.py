# Define a class called 'Car'
class Car:
    # Constructor to initialize object properties
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Method to display car details
    def display_details(self):
        print(f"Car Details: {self.year} {self.color} {self.make} {self.model}")

    # Method to start the car
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running.")

    # Method to stop the car
    def stop_engine(self):
        print(f"The {self.make} {self.model}'s engine is now stopped.")


# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020, "Silver")
car2 = Car("Honda", "Civic", 2022, "Blue")

# Accessing object methods and properties
car1.display_details()
car1.start_engine()
car1.stop_engine()

print()  # Empty line for better readability

car2.display_details()
car2.start_engine()
car2.stop_engine()
