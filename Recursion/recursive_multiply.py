def recursive_multiply1(x, y):
    if x == 1:
        return y
    else:
        return y + recursive_multiply1(x-1, y)


def recursive_multiply(x, y):
    # This cuts down on the total number of recursive calls:
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)


print(recursive_multiply1(4, 5))
print(recursive_multiply1(40, 50))
print(recursive_multiply1(32, 51))
# print(recursive_multiply1(2000, 500))

print(recursive_multiply(4, 5))
print(recursive_multiply(40, 50))
print(recursive_multiply(32, 51))
print(recursive_multiply(2000, 500))
