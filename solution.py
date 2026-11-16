menu = {
    "Dosa": 80,
    "Idli": 40,
    "Thali": 150,
    "Tea": 20
}


def get_subtotal(cart):
    total = 0
    for cart_item in cart:
        total = total + cart_item[2]
    return total


def get_discount(subtotal):
    if subtotal > 500:
        return subtotal * 0.10
    return 0


def get_gst(amount):
    return amount * 0.05


def get_grand_total(amount, gst):
    return amount + gst


cart = []

while True:
    item = input("Order item: ").strip().capitalize()

    if item == "Generate bill":
        break

    if item not in menu:
        print("Item not on the menu. Available: Dosa, Idli, Thali, Tea")
        continue

    qty_text = input("Quantity: ").strip()

    if not qty_text.isdigit():
        print("Invalid quantity. Enter a whole number.")
        continue

    quantity = int(qty_text)

    if quantity < 1:
        print("Quantity must be at least 1.")
        continue

    item_total = menu[item] * quantity
    cart.append((item, quantity, item_total))
    print(item, "x" + str(quantity), "added | Amount:", item_total)

if len(cart) > 0:
    subtotal = get_subtotal(cart)
    discount = get_discount(subtotal)
    after_discount = subtotal - discount
    gst = get_gst(after_discount)
    grand_total = get_grand_total(after_discount, gst)

    print("\n--- FINAL BILL ---")
    for cart_item in cart:
        print(cart_item[0], "x" + str(cart_item[1]), "=", cart_item[2])

    print("Subtotal:", subtotal)
    print("Discount:", format(discount, ".2f"))
    print("GST (5%):", format(gst, ".2f"))
    print("Grand Total:", format(grand_total, ".2f"))
else:
    print("No items ordered.")