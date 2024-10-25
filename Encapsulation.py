class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public member
        self._balance = balance  # Protected member (convention, not enforced)
        self.__password = "secret"  # Private member

    # Getter method for balance (public method to access protected member _balance)
    def get_balance(self):
        return self._balance

    # Setter method for balance (ensures valid balance change)
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    # Private method to change password (only accessible within the class)
    def __change_password(self, new_password):
        self.__password = new_password
        print("Password changed successfully.")

    # Public method to interact with private method
    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__change_password(new_password)
        else:
            print("Incorrect password. Cannot change password.")


# Create an Account object
account = Account("John", 1000)

# Accessing the public and protected members via methods
print(f"Initial Balance: {account.get_balance()}")

account.deposit(500)
print(f"Balance after deposit: {account.get_balance()}")

account.withdraw(200)
print(f"Balance after withdrawal: {account.get_balance()}")

# Accessing the protected member (not recommended but possible)
print(f"Directly accessing protected balance: {account._balance}")

# Accessing the private member __password (will result in error)
# print(account.__password)  # Uncommenting this line will raise an AttributeError

# Using public method to change the password
account.change_password("secret", "new_secret")
