# Iterative length calculation: O(n)
def iterative_str_len(input_str):
    input_str_len = 0
    for i in range(len(input_str)):
        input_str_len += 1
    return input_str_len


# Recursive length calculation: O(n)
def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])


input_str = "LucidProgramming"
print(len(input_str))
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))


