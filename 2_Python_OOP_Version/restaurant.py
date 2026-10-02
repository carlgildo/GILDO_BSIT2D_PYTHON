class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, food, quantity):
        subtotal = food.price * quantity
        self.items.append((food, quantity, subtotal))

    def calculate_total(self):
        total = 0

        for food, quantity, subtotal in self.items:
            total += subtotal

        return total

    def display_receipt(self):
        print("\n========== RECEIPT ==========")

        if not self.items:
            print("No items ordered.")
            return

        for food, quantity, subtotal in self.items:
            print(f"{food.name} x{quantity} - ₱{subtotal}")

        print("-----------------------------")
        print(f"Total: ₱{self.calculate_total()}")
        print("=============================")


class FastFoodRestaurant:
    def __init__(self):
        self.menu = [
            FoodItem("Burger", 50),
            FoodItem("Fries", 35),
            FoodItem("Chicken", 85),
            FoodItem("Spaghetti", 60),
            FoodItem("Soft Drink", 30)
        ]

    def display_menu(self):
        print("\n===== FAST FOOD MENU =====")

        for number, food in enumerate(self.menu, start=1):
            print(f"{number}. {food.name} - ₱{food.price}")

        print("0. Finish Order")
        print("==========================")

    def take_order(self):
        order = Order()

        while True:
            self.display_menu()

            try:
                choice = int(input("Enter your choice: "))

                if choice == 0:
                    break

                if choice < 1 or choice > len(self.menu):
                    print("Invalid choice. Please try again.")
                    continue

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                food = self.menu[choice - 1]

                order.add_item(food, quantity)

                print(f"{quantity} {food.name}(s) added to your order.")

            except ValueError:
                print("Please enter a valid number.")

        return order