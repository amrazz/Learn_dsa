# bubble sort using for loop


def bubble_sort(arr):
    count = 0
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    print(count)
    return arr


arr = [1, 31, 34, 22, 12, 10, 2, 6]
print("THis is the bubble sort", bubble_sort(arr))

# bubble sort using while loop


def bubble_sort(arr):
    while True:
        a = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                a = True

        if not a:
            break

    return arr


# Time complexity of bubble sort is O(n^2)
# space complexity of Bubblee sort is O(1)


# SELECTION SORT


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(min + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr


print("This is the selection sort", selection_sort(arr))


# Time complexity O(n^2)
# Space complexity O(1)


# INSERTION SORT


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


print("This is the insertion sort:", insertion_sort(arr))

# time complexity O(n^2), space complexity O(1)


def MergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        MergeSort(left)
        MergeSort(right)

        lp = 0
        rp = 0
        fp = 0

        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                arr[fp] = left[lp]
                lp += 1
            else:
                arr[fp] = right[rp]
                rp += 1
            fp += 1

        while lp < len(left):
            arr[fp] = left[lp]
            fp += 1
            lp += 1

        while rp < len(right):
            arr[fp] = right[rp]
            fp += 1
            rp += 1

    return arr


print("This is the merge sort", MergeSort(arr))


# Space complexity : O(n), Time complexity : O(nlogn)


def Quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return Quick_sort(left) + middle + Quick_sort(right)


print("This is the quick sort", Quick_sort(arr))


# Space complexity : O(log n)), Time complexity : O(n^2)
