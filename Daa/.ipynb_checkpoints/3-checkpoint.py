#  Write a program to solve a fractional Knapsack problem using a greedy method
# 23CO132

def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0

    return total_value


n = int(input("Enter the number of items: "))

items = []
for i in range(n):
    weight = float(input(f"Enter weight of item {i + 1}: "))
    value = float(input(f"Enter value of item {i + 1}: "))
    items.append((weight, value))

capacity = float(input("Enter the knapsack capacity: "))

max_value = fractional_knapsack(capacity, items)

print("Maximum value in knapsack:", max_value)


# Enter the number of items: 3 
# Enter weight of item 1: 10
# Enter value of item 1: 60
# Enter weight of item 2: 20
# Enter value of item 2: 100
# Enter weight of item 3: 30
# Enter value of item 3: 120
# Enter the knapsack capacity: 50
# Maximum value in knapsack: 240.0