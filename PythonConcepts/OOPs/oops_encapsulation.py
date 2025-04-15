"""
This is a file that contains the code for the bank account.
"""


class BankAccount:
    """
    This is a class that defines the bank account. (Public, Protected, and Private attributes.)
    Deposit, Withdraw, and Retrieve Balance
    """

    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._bank_name = "HDFC Bank"  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Public method to modify private balance"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Public method with controlled access"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    @staticmethod
    def default_balance():
        """Added static property to show default message."""
        return "Current balance is too low."
    
    @property
    def get_balance(self):
        """Public method to access private balance"""
        if self.__balance:
            return f"Current balance: ₹{self.__balance}"
        return self.default_balance()
        


# Creating an object
account = BankAccount("123456789", 5000)

# Accessing Public attribute
print(account.account_number)  # ✅ Allowed: 123456789

# Accessing Protected attribute
print(account._bank_name)  # ✅ Allowed (but not recommended): HDFC Bank

# Trying to access Private attribute
# print(account.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'

# Correct way to access private data
# print(account.get_balance())  # ✅ Allowed: Current balance: ₹5000

# Modifying balance using controlled methods
account.deposit(2000)  # ✅ Deposited ₹2000. New balance: ₹7000
account.withdraw(7000)  # ✅ Withdrew ₹1000. Remaining balance: ₹6000
print(account.get_balance)
