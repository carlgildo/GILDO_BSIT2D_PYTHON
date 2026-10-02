def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Please enter a valid number.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")