# DAA3. Write a program to solve a fractional Knapsack problem using a greedy method.


def fractional_knapsack(items, capacity):
    # Each item is represented as (item_id, weight, value)
    items.sort(key=lambda item: item[2] / item[1], reverse=True)

    total_value = 0.0
    selected_items = []

    for item_id, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            # Take the complete item
            selected_items.append((item_id, 1.0))
            total_value += value
            capacity -= weight
        else:
            # Take only the fraction that fits
            fraction = capacity / weight
            selected_items.append((item_id, fraction))
            total_value += value * fraction
            capacity = 0

    return selected_items, total_value


items = [
    ("A", 10, 60),
    ("B", 20, 100),
    ("C", 30, 120)
]

capacity = 50

selected_items, max_value = fractional_knapsack(items, capacity)

print("Selected items and fractions:")
for item_id, fraction in selected_items:
    print(f"Item {item_id}: {fraction:.2f}")

print("Maximum value:", max_value)