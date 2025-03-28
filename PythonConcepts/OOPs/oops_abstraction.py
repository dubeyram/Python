"""
This is a file that contains the code for the abstract class.
"""

from abc import ABC, abstractmethod


# Abstract Class
class Payment(ABC):
    """
    This is an abstract class that defines the payment method.
    """

    def __init__(self, amount):
        self.amount = amount  # Common attribute

    @abstractmethod
    def process_payment(self):
        """Abstract method to be implemented by subclasses"""
        pass


# Concrete Class 1: CreditCard Payment
class CreditCardPayment(Payment):
    def process_payment(self):
        return f"Processing Credit Card payment of ₹{self.amount}"


# Concrete Class 2: PayPal Payment
class PayPalPayment(Payment):
    def process_payment(self):
        return f"Processing PayPal payment of ₹{self.amount}"


# Concrete Class 3: UPI Payment
class UPIPayment(Payment):
    def process_payment(self):
        return f"Processing UPI payment of ₹{self.amount}"


# Creating instances
payment1 = CreditCardPayment(1000)
payment2 = PayPalPayment(500)
payment3 = UPIPayment(300)

# Calling process_payment() - Different implementations but same interface
print(payment1.process_payment())  # Output: Processing Credit Card payment of ₹1000
print(payment2.process_payment())  # Output: Processing PayPal payment of ₹500
print(payment3.process_payment())  # Output: Processing UPI payment of ₹300
