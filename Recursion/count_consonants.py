vowels = "aeiou"


def count_consonants_iterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            count += 1
    return count


def count_consonants_recursive(input_str):
    if input_str == "":
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + count_consonants_recursive(input_str[1:])
    else:
        return count_consonants_recursive(input_str[1:])


input_str = "Welcome to Educative!"
print(input_str)
print(count_consonants_iterative(input_str))
print(count_consonants_recursive(input_str))
input_str = "abc de"
print(input_str)
print(count_consonants_iterative(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(count_consonants_recursive(input_str))