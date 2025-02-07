from product import Product
from user import User
from cart import Cart

def main():
    # Create Users
    user1 = User("Kevin Vivian", "Premium")
    user2 = User("John Doe", "Regular")

    # Create Products
    product1 = Product("Laptop", 1500)
    product2 = Product("Phone", 800)
    product3 = Product("Headphones", 200)

    # Test Cart for User 1 (Premium User)
    print("\n=== Testing Cart for Premium User ===")
    cart1 = Cart(user1)

    # Add products to the cart
    cart1.add_product(product1)
    cart1.add_product(product2)

    # Display cart contents
    cart1.display_cart()

    # Calculate total without discount
    print(f"Total before discount: ${cart1.calculate_total()}")

    # Apply discount and display total
    cart1.checkout()

    # Test Cart for User 2 (Regular User)
    print("\n=== Testing Cart for Regular User ===")
    cart2 = Cart(user2)

    # Add products to the cart
    cart2.add_product(product2)
    cart2.add_product(product3)

    # Display cart contents
    cart2.display_cart()

    # Calculate total without discount
    print(f"Total before discount: ${cart2.calculate_total()}")

    # Apply discount and display total
    cart2.checkout()

    # Test Empty Cart
    print("\n=== Testing Empty Cart ===")
    empty_cart = Cart(user1)
    empty_cart.display_cart()
    print(f"Total before discount: ${empty_cart.calculate_total()}")
    empty_cart.checkout()

if __name__ == "__main__":
    main()
