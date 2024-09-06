class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item_name, price, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if price < 0:
            raise ValueError("Price must be a non-negative number.")
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
            self.cart[item_name]['price'] = price
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name):
        if item_name in self.cart:
            del self.cart[item_name]
        else:
            raise KeyError(f"Item '{item_name}' not found in the cart.")

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def display_cart(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            print(f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Total':<10}")
            print("-" * 50)
            for item_name, details in self.cart.items():
                item_total = details['price'] * details['quantity']
                print(f"{item_name:<20} ${details['price']:<10.2f} {details['quantity']:<10} ${item_total:<10.2f}")
            print("-" * 50)
            print(f"Total Cost: ${self.calculate_total():.2f}")

def main():
    cart = ShoppingCart()
    
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display cart")
        print("4. Calculate total")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            item_name = input("Enter the item name: ").strip()
            price = float(input("Enter the price of the item: ").strip())
            quantity = int(input("Enter the quantity of the item: ").strip())
            try:
                cart.add_item(item_name, price, quantity)
                print(f"Added {quantity} {item_name}(s) to the cart.")
            except ValueError as e:
                print(e)
        
        elif choice == '2':
            item_name = input("Enter the item name to remove: ").strip()
            try:
                cart.remove_item(item_name)
                print(f"Removed {item_name} from the cart.")
            except KeyError as e:
                print(e)
        
        elif choice == '3':
            cart.display_cart()
        
        elif choice == '4':
            print(f"Total Cost: ${cart.calculate_total():.2f}")
        
        elif choice == '5':
            print("Good Bye")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
