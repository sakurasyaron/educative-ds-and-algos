def find(data, find_val):
    for i in range(len(data)):
        if data[i] == find_val:
            return i
    return None


def find_bs(data, find_val):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low+high)//2
        if data[mid] < find_val:
            low = mid + 1
        elif data[mid] > find_val:
            high = mid - 1
        else:
            if mid - 1 < 0 or data[mid - 1] != find_val:
                return mid
            high = mid - 1


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
print(find(A, target))
print(find_bs(A, target))
