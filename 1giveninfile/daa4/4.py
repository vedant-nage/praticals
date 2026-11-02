# DAA4. Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and 
# bound strategy.

def knapsack_01(weights, values, capacity):
    n = len(weights)

    # dp[i][w] = maximum value using first i items
    # with knapsack capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(capacity + 1):
            # Do not take the current item
            dp[i][w] = dp[i - 1][w]

            # Take the item if it fits
            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    # Trace back to find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, selected_items = knapsack_01(weights, values, capacity)

print("Maximum value:", max_value)
print("Selected item indexes:", selected_items)