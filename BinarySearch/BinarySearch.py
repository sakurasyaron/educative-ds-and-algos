def linear_search(data, find_val):
    for i in range(len(data)):
        if data[i] == find_val:
            return True
    return False


def binary_search_iterative(data, find_val):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if find_val == data[mid]:
            return True
        elif find_val < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_recursive(data, find_val, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if find_val == data[mid]:
            return True
        elif find_val < data[mid]:
            return binary_search_recursive(data, find_val, low, mid - 1)
        else:
            return binary_search_recursive(data, find_val, mid + 1, high)


a = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 37
print(linear_search(a, target))
print(binary_search_recursive(a, target, 0, len(a) - 1))
print(binary_search_iterative(a, target))
