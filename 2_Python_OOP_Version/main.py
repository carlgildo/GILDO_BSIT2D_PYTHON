from restaurant import FastFoodRestaurant


def main():
    print("WELCOME TO OUR FAST FOOD RESTAURANT!")

    restaurant = FastFoodRestaurant()

    order = restaurant.take_order()

    order.display_receipt()

    print("\nThank you for ordering!")


if __name__ == "__main__":
    main()