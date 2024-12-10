def binary_search(arr: list[int], key: int) -> int:
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if key == arr[mid]:
            return mid

        if key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5]
key = 3

print(binary_search(arr, key))
