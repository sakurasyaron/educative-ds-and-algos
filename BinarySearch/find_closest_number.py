def find_closest_number(data, target):
    min_diff = float('inf')
    low = 0
    high = len(data) - 1
    closest_num = None

    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]

    while low <= high:
        mid = (low+high)//2
        # Ensure you do not read beyond the bounds of the list
        if mid+1 < len(data):
            min_diff_right = abs(data[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(data[mid-1] - target)

        # Check if the absolute value between left nd right elements are
        # smaller than any seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[mid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[mid+1]

        # Move the mid-point appropriately as is done
        # via binary search.
        if data[mid] < target:
            low = mid+1
        elif data[mid] > target:
            high = mid-1
        # If the element itself is the target, the closest
        # number to it is itself. Return the number.
        else:
            return data[mid]
    return closest_num


A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 4, 6, 7, 8, 8, 9]
print(find_closest_number(A1, 11))
print(find_closest_number(A2, 8))
