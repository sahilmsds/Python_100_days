orders = [
    ("Alice", 50),
    ("Bob", 30),
    ("Alice", 20),
    ("Charlie", 40),
    ("Bob", 50),
    ("Alice", 30),
]

def top_customer(orders):
    total_spent = {}
    for name, cost in orders:
        if name in total_spent:
            total_spent[name] += cost
        else:
            total_spent[name] = cost
    most_spent = 0
    top_customer = []
    for name, total in total_spent.items():
        if total > most_spent:
            most_spent = total
            top_customer = [name]
        elif total == most_spent:
            top_customer.append(name)
    
    for name, cost in total_spent.items():
        print(f"{name}: {cost}")
    
    print(f"Top customer(s):", ",".join(top_customer))

top_customer(orders)