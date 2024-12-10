def linear_search(arr: list[int], key: int) -> int:
    for i, n in enumerate(arr):
        if n == key:
            return i

    return -1


arr = [1, 2, 3, 4, 5]
key = 9

print(linear_search(arr, key))
