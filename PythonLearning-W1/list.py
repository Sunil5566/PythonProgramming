raw_orders = [
    ("Alice", "Latte", 4.50),
    ("Bob", "Espresso", 3.00),
    ("Alice", "Muffin", 3.50),
    ("Charlie", "Latte", 4.50),
    ("Bob", "Espresso", 3.00), 
]



# All items sold: ['Latte', 'Espresso', 'Muffin', 'Latte', 'Espresso']
# Unique customers: {'Alice', 'Bob', 'Charlie'}
# Customer totals: {'Alice': 8.0, 'Bob': 6.0, 'Charlie': 4.5}
# Most expensive order: Alice bought a Latte for $4.5

a = raw_orders.get(1,1)
print(a)