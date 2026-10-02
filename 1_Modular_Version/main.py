from menu import MENU
from display import display_menu, display_receipt
from input_functions import get_choice, get_quantity
from order_functions import add_order, calculate_total


def main():
    print("WELCOME TO OUR FAST FOOD RESTAURANT!")

    order = []

    while True:
        display_menu(MENU)

        choice = get_choice()

        if choice == 0:
            break

        if choice not in MENU:
            print("Invalid choice. Please try again.")
            continue

        item, price = MENU[choice]

        quantity = get_quantity()

        add_order(order, item, quantity, price)

        print(f"{quantity} {item}(s) added to your order.")

    total = calculate_total(order)

    display_receipt(order, total)

    print("\nThank you for ordering!")


if __name__ == "__main__":
    main()