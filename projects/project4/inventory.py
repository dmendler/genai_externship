inventory = {
    "apple": (10, 2.5),  # (quantity, price)
    "banana": (20, 1.2),
}

def add_item(name: str, quantity: int, price: float) -> None:
    """Add an item to the inventory."""
    print(f"Adding a new item: {name}")
    data = (quantity, price)
    inventory[name] = data

def remove_item(name: str) -> None:
    """Remove an item from the inventory."""
    print(f"Removing an item: {name}")
    if name in inventory:
        inventory.pop(name)
    else:
        print(f"Item {name} not found in inventory.")

def update_item(name: str, quantity: int, price: float) -> None:
    """Update an existing item in the inventory."""
    print(f"Updating an item: {name}")
    data = (quantity, price)
    inventory[name] = data

def display_inventory() -> None:
    """Display the current inventory."""
    for name, (quantity, price) in inventory.items():
        print(f"Item: {name}, Quantity: {quantity}, Price: ${price}")

def calculate_total_value() -> float:
    """Calculate the total value of the inventory."""
    total_value = 0.0
    for quantity, price in inventory.values():
        total_value += quantity * price
    return total_value

def main() -> None:
    """Main function to demonstrate inventory management."""
    print("Welcome to the Inventory Manager!")
    print("Current Inventory:")
    display_inventory()

    while True:
        print("\nOptions:")
        print("a. Add Item")
        print("r. Remove Item")
        print("u. Update Item")
        print("q. Exit")

        choice = input("Enter your choice: ")
        
        if choice == 'a':
            try:
                name = input("Enter item name: ")
                quantity = int(input("Enter item quantity: "))
                price = float(input("Enter item price: "))
                add_item(name, quantity, price)
            except ValueError:
                print("Invalid input. Please enter an integer for quantity and a float for price.")
                continue
        elif choice == 'r':
            name = input("Enter item name to remove: ")
            remove_item(name)
        elif choice == 'u':
            name = input("Enter item name to update: ")
            if name not in inventory:
                print(f"Item {name} not found in inventory.")
                continue
            quantity = int(input("Enter new item quantity: "))
            price = float(input("Enter new item price: "))
            update_item(name, quantity, price)
        elif choice == 'q':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

        print("\nUpdated inventory:")
        display_inventory()
        print(f"Total value of inventory: ${calculate_total_value():.2f}")

if __name__ == "__main__":
    main()