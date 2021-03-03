def intersect_sorted_arrays(A, B):
    i, j = 0, 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


A1 = [2, 3, 3, 5, 7, 11]
B1 = [3, 3, 7, 15, 31]
# print(set(A1).intersection(B1))
print(intersect_sorted_arrays(A1, B1))
