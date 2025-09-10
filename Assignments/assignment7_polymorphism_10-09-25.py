# Scenario:
# You are building the backend logic of a product and order management system for an e-commerce 
# platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, 
# and different order behaviors dynamically.
 
# Q1. Product Search System (Static Polymorphism)

# Problem Statement:
# Implement a class ProductSearch that allows searching products with different combinations of 
# criteria (name, category, price range).
 
# Requirements:
# Use default arguments and/or *args, **kwargs to simulate method overloading.
# Allow the following types of searches:
# Only by name
# Name and category
# Name, category, and price range
 
# Q2. Cart System with Quantity Variations (Static Polymorphism)
 
# Problem Statement:
# Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
 
# Requirements:
# Add multiple products at once with name and quantity
# Simulate static polymorphism using variable arguments

# Q3. Discount Application (Static Polymorphism)
 
# Problem Statement:
# Create a class Discount that allows applying different types of discounts: 
# Flat discount
# Percentage discount
# Buy One Get One
# Use static polymorphism to overload the method using default parameters or *args
 
# Q4. Payment System (Dynamic Polymorphism)

# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. 
# Each should override a method pay().
 
# Requirements:
# Override pay() method in each class to simulate different payment methods


class ProductSearch:
    def search(self, name=None, category=None, price_range=None):
        if name and not category and not price_range:
            return f"Searching for products with name: {name}"
        elif name and category and not price_range:
            return f"Searching for products with name: {name} in category: {category}"
        elif name and category and price_range:
            return f"Searching for products with name: {name} in category: {category} within price range: {price_range}"
        else:
            return "Please provide at least a product name to search."

product = ProductSearch()
print(product.search(name="Laptop"))
print(product.search(name="Laptop", category="Electronics"))
print(product.search(name="Laptop", category="Electronics", price_range=(500, 1500)))

#####################################################################################

class Cart:
    def __init__(self):
        self.items = {}

    def add_products(self, **kwargs):
        for product, quantity in kwargs.items():
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
        return f"Current cart items: {self.items}"
    
cart = Cart()
print(cart.add_products(Laptop=1, Mouse=2))
print(cart.add_products(Keyboard=1, Monitor=1))
print(cart.add_products(WiFi=1, Bluetooth=1))

#####################################################################################

class Discount:
    def apply_discount(self, discount_type, amount=None, percentage=None):
        if discount_type == "flat" and amount:
            return f"Applying flat discount of {amount}"
        elif discount_type == "percentage" and percentage:
            return f"Applying percentage discount of {percentage}%"
        elif discount_type == "BO-GO":
            return "Applying Buy One Get One discount"
        else:
            return "Invalid discount type or parameters"
        
discount = Discount()
print(discount.apply_discount("flat", amount=50))
print(discount.apply_discount("percentage", percentage=10))
print(discount.apply_discount("BO-GO"))

#####################################################################################

class Payment:
    def pay(self):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(Payment):
    def pay(self):
        return "Processing payment through Credit Card"

class UPIPayment(Payment):
    def pay(self):
        return "Processing payment through UPI"

class CODPayment(Payment):
    def pay(self):
        return "Processing payment through Cash on Delivery"

# Testing the payment methods
payments = [CreditCardPayment(), UPIPayment(), CODPayment()]
for payment in payments:
    print(payment.pay())

