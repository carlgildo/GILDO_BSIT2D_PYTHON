def display_menu(menu):
    print("\n===== FAST FOOD MENU =====")

    for number, (item, price) in menu.items():
        print(f"{number}. {item} - ₱{price}")

    print("0. Finish Order")
    print("==========================")


def display_receipt(order, total):
    print("\n========== RECEIPT ==========")

    if not order:
        print("No items ordered.")
        return

    for item, quantity, subtotal in order:
        print(f"{item} x{quantity} - ₱{subtotal}")

    print("-----------------------------")
    print(f"Total: ₱{total}")
    print("=============================")