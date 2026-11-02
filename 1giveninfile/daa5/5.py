# DAA5. Write a program to generate binomial coefficients using dynamic programming.

def binomial_coefficients(n):
    # Create a table with n + 1 rows and n + 1 columns
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i + 1):
            # First and last coefficients in each row are 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # Pascal's identity
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp


# n = int(input("Enter n: "))
n = 5
table = binomial_coefficients(n)

print(f"Binomial coefficients for n = {n}:")
for i in range(n + 1):
    print(*table[i][:i + 1])