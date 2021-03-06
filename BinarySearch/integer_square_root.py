def integer_square_root1(k):
    low = 0
    high = k
    root = 0
    while low <= high:
        mid = (low + high)//2
        if mid*mid == k or mid == root:
            return mid
        elif mid*mid < k:
            low = mid
            if mid > root:
                root = mid
        else:
            high = mid
    return root


def integer_square_root(k):
    low = 0
    high = k
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


print(integer_square_root(300))
print(integer_square_root(12))
print(integer_square_root(1000))
print(integer_square_root(625))
