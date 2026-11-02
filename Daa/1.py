#1. Write a program non-recursive and recursive program to calculate Fibonacci numbers and 
# analyze their time and space complexity.

# Fibonacci using both iterative and recursive methods

def fibonacci_iterative(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter the number of terms: "))

print("Iterative Fibonacci:")
fibonacci_iterative(n)

print("\nRecursive Fibonacci:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print("\n\nTime and Space Complexity:")
# print("Iterative: Time O(n), Space O(1)")
# print("Recursive: Time O(2^n), Space O(n)")



