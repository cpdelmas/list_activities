order1 = str(input("Enter order 1: "))
order2 = str(input("Enter order 2: "))
order3 = str(input("Enter order 3: "))
order4 = str(input("Enter order 4: "))
order5 = str(input("Enter order 5: "))
orders = [order1, order2, order3, order4, order5]

print(f"Original orders: {orders}")
add = str(input("Enter additional order: "))
orders.append(add)
print(f"Updated orders: {orders}")

prio = str(input("Enter priority order: "))
orders.insert(0, prio)
print(f"Updated orders: {orders}")

search_item = input("Enter a food item to search for: ").strip()
item_count = orders.count(search_item)

if item_count > 0:
    first_index = orders.index(search_item)
    print(f"'{search_item}' found {item_count} time(s). First index: {first_index}")
else:
    print("Order not found.")


cancel_item = input("Enter an order to cancel: ").strip()
if cancel_item in orders:
    orders.remove(cancel_item)
    print(f"{cancel_item} has been canceled.")
else:
    print("Order not found. Nothing removed.")


if len(orders) > 0:
    removed_item = orders.pop()
    print(f"Removed last order: {removed_item}")


orders.sort()

print("===== FINAL ORDER REPORT =====-")
print("Final sorted orders:", orders)
print("Total remaining orders:", len(orders))