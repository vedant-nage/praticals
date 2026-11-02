#  Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and 
# bound strategy.
# 23CO132


def knapsack(weights, values, capacity):
    n = len(weights)

    # Create a DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter knapsack capacity: "))

max_value = knapsack(weights, values, capacity)

print("Maximum value:", max_value)






# Enter number of items: 3
# Enter weight of item 1: 10
# Enter value of item 1: 60
# Enter weight of item 2: 20
# Enter value of item 2: 100
# Enter weight of item 3: 30
# Enter value of item 3: 120
# Enter knapsack capacity: 50

# Maximum value: 220