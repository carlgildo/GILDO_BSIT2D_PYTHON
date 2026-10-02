def add_order(order, item, quantity, price):
    subtotal = price * quantity

    order.append((item, quantity, subtotal))

    return subtotal


def calculate_total(order):
    total = 0

    for item, quantity, subtotal in order:
        total += subtotal

    return total