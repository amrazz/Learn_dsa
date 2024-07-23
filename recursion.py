# def recursive_sum(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + recursive_sum(arr[1:])


# arr = [1, 2, 3, 4, 5]
# print("Array:", arr)
# print("Sum of array elements (recursive):", recursive_sum(arr))


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(21))

def fibo(position, memory = {}):
    if position in memory:
        return memory[position]
    if position <= 2:
        return 1
    memory[position] = fibo(position-1, memory) + fibo(position-2, memory)
    return memory[position]

print(fibo(9, {}))


def fibo(position):
    arr = [0] * position
    arr[0] = 1
    arr[1] = 1
    for i in range(2, len(arr)):
        arr[i] = arr[i-1] + arr[i-2]
    return arr

print(fibo(9))

# print(0)
# print(1)
# count = 2