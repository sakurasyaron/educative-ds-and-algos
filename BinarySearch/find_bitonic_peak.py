def find_highest_num(data):
    low = 0
    high = len(data) - 1
    # Require at least 3 elements for a bitonic sequence.
    if len(data) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        mid_left = data[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = data[mid + 1] if mid + 1 < len(data) else float('inf')
        if mid_left < data[mid] < mid_right:
            low = mid + 1
        elif mid_left > data[mid] > mid_right:
            high = mid - 1
        elif mid_left < data[mid] and mid_right < data[mid]:
            return data[mid]
    return None


# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_num(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_num(A))
A = [1, 2, 3, 4, 5]
print(find_highest_num(A))
A = [5, 4, 3, 2, 1]
print(find_highest_num(A))
