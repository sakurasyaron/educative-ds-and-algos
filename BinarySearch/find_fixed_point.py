# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(data):
    for i in range(len(data)):
        if data[i] == i:
            return data[i]
    return None


# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(data):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low+high)//2
        if data[mid] < mid:
            low = mid + 1
        elif data[mid] > mid:
            high = mid - 1
        else:
            return data[mid]
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]

print("Linear Approach")
print(A1)
print(find_fixed_point_linear(A1))
print(A2)
print(find_fixed_point_linear(A2))
print(A3)
print(find_fixed_point_linear(A3))
print("Binary Search Approach")
print(A1)
print(find_fixed_point(A1))
print(A2)
print(find_fixed_point(A2))
print(A3)
print(find_fixed_point(A3))
