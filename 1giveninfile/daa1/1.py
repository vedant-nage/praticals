# DAA1. Write a program to calculate Fibonacci numbers and find its step count.
def fibonacci(n):
    a, b = 0, 1
    step_count = 0

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        step_count += 1

    print("\nStep count:", step_count)


n = int(input("Enter number of Fibonacci terms: "))
fibonacci(n)