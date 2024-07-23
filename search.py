arr = [34, 351, 62, 63, 23, 7, 82, 55]
target = 82


def linear_search(arr, target):
    step = 0
    for i in range(0, len(arr)):
        step += 1
        if arr[i] == target:
            return arr[i], i, step
    return str("No result found.")


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid], mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


print(binary_search(arr, target))
print(linear_search(arr, target))


def fibnocci(n):
    if n == 0 or n == 1:
        return 1
    return fibnocci(n-1) + fibnocci(n-2)

print(fibnocci(8))



    