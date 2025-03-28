"""
This is a file that contains the code for the abstraction, inheritance, encapsulation and polymorphism.
"""

from abc import ABC, abstractmethod


# 🔹 Abstraction: Define an Abstract Class
class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount  # 🔹 Encapsulation: Private variable

    @abstractmethod
    def process_payment(self):
        """Abstract method to be implemented by child classes"""
        pass

    def get_amount(self):  # Getter method (Encapsulation)
        return self.__amount


# 🔹 Inheritance: Child classes inherit from Payment
class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.__card_number = card_number  # Encapsulation: Private card number

    def process_payment(self):  # 🔹 Polymorphism: Overriding process_payment
        return f"Paid ₹{self.get_amount()} using Credit Card ending with {self.__card_number[-4:]}"


# 🔹 Inheritance: Child classes inherit from Payment
class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.__email = email  # Encapsulation: Private email

    def process_payment(self):  # 🔹 Polymorphism: Overriding process_payment
        return f"Paid ₹{self.get_amount()} using PayPal (Email: {self.__email})"


# 🔹 Inheritance: Child classes inherit from Payment
class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.__upi_id = upi_id  # Encapsulation: Private UPI ID

    def process_payment(self):  # 🔹 Polymorphism: Overriding process_payment
        return f"Paid ₹{self.get_amount()} using UPI ID {self.__upi_id}"


# 🔹 Using Polymorphism: Same method call, different behaviors
payments = [
    CreditCardPayment(1000, "1234-5678-9876-5432"),
    PayPalPayment(500, "user@example.com"),
    UPIPayment(750, "user@upi"),
]

# Processing all payments
for payment in payments:
    print(payment.process_payment())  # Calls different implementations
