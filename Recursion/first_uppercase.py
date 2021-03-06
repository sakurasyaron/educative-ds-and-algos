def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No Uppercase character found"


def find_uppercase_recursive(input_str, i=0):
    if input_str[i].isupper():
        return input_str[i]
    if i == len(input_str) - 1:
        return "No Uppercase character found"
    return find_uppercase_recursive(input_str, i+1)


str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"
print(find_uppercase_iterative(str_1))
print(find_uppercase_iterative(str_2))
print(find_uppercase_iterative(str_3))
print(find_uppercase_recursive(str_1))
print(find_uppercase_recursive(str_2))
print(find_uppercase_recursive(str_3))