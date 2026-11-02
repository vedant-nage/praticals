import random
import time


# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return (
        deterministic_quick_sort(left)
        + [pivot]
        + deterministic_quick_sort(right)
    )


# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    remaining = arr[:pivot_index] + arr[pivot_index + 1:]

    left = [x for x in remaining if x <= pivot]
    right = [x for x in remaining if x > pivot]

    return (
        randomized_quick_sort(left)
        + [pivot]
        + randomized_quick_sort(right)
    )


# Input
# arr = list(map(int, input("Enter elements: ").split()))
arr = [1,3,4,2,8,5,4,0]

# Deterministic Quick Sort
start = time.perf_counter()
sorted1 = deterministic_quick_sort(arr.copy())
time1 = time.perf_counter() - start

# Randomized Quick Sort
start = time.perf_counter()
sorted2 = randomized_quick_sort(arr.copy())
time2 = time.perf_counter() - start

print("Deterministic Quick Sort:", sorted1)
print("Randomized Quick Sort:", sorted2)

print("Deterministic Time:", time1)
print("Randomized Time:", time2)

