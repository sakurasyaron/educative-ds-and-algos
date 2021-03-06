def find1(A):
    low = 0
    high = len(A) - 1
    min_a = A[low]
    min_index = low
    while low <= high:
        mid = (low + high) // 2
        l = A[low]
        h = A[high]
        m = A[mid]
        if h < l:
            if m < h:
                if min_a > m:
                    min_a = m
                    min_index = mid
                high = mid - 1
            else:
                if min_a > h:
                    min_a = h
                    min_index = high
                low = mid + 1
        else:
            if l < m:
                if min_a > l:
                    min_a = l
                    min_index = low
                high = low - 1
            else:
                if min_a > m:
                    min_a = m
                    min_index = mid
                low = mid + 1
    return min_index


def find(A):
    low = 0
    high = len(A) - 1
    while low < high:
        mid = (low + high)//2
        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid
    return low


A1 = [4, 5, 6, 7, 1, 2, 3]
print(find(A1))

