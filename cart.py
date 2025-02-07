from product import Product
from user import User

class Cart:
    def __init__(self, user):
        self.products = []
        self.user = user

    def add_product(self, product):
        self.products.append(product)
        print(product.get_name(), 'added to cart')

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def display_cart(self):
        print(f"User: {self.user.get_username()} (Type: {self.user.get_usertype()})")
        if self.products:
            for product in self.products:
                print(f"-Product: {product.get_name()}, Price: ${product.get_price()}")
        else:
            print("The cart is empty")

    def apply_discount(self):
        total = self.calculate_total()
        if self.user.get_usertype() == 'Premium':
            print("Applying 20% discount for premium user")
            return total * 0.8
        else:
            print("No discount for regular user")
            return total

    def checkout(self):
        total = self.apply_discount()
        print(f"Total after discount: ${total}")