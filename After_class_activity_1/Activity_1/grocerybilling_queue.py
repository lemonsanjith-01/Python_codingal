# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True


# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
while billing:
    customer_name = input("Enter customer name: ")
    item_count = int(input(f"Hello {customer_name}! How many items are you buying? "))
    if item_count <= 0:
        print("Invalid item count. Please enter a positive number.")
        continue

    customer_total = 0
    item_number = 1
    while item_number <= item_count:
        item_name = input(f"Enter the name of item {item_number}: ")
        price = int(input(f"Enter the price of {item_name}: "))
        quantity = int(input(f"Enter the quantity of {item_name}: "))
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity. Please enter positive numbers.")
            continue
        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        customer_total += item_total

        if quantity < 50:
            low_price_items += 1
        elif quantity <= 100:
            medium_price_items += 1
        else:
            high_price_items += 1

        item_number += 1

# ---------- PART 6: finish the customer, ask about the next ----------
    customers_served += 1
    total_sales += customer_total
    print(f"Customer {customer_name}'s total: ${customer_total}")

    next_customer = input("Next customer? (yes/no): ")
    if next_customer != "yes":
        billing = False
# ---------- PART 7: the NESTED for report ----------
for band, items in [("Low Price", low_price_items), ("Medium Price", medium_price_items), ("High Price", high_price_items)]:
    print(f"{band} Items: ", end="")
    for _ in range(items):
        print("*", end="")
        print(customers_served, total_sales)