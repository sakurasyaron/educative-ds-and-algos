def str_to_int(input_str):
    output = 0
    if input_str[0] == "-":
        is_neg = True
        input_str = input_str[1:]
    else:
        is_neg = False
    for i in input_str:
        output = output*10 + (ord(i)-ord("0"))
    if is_neg:
        output *= -1
    return output


print(str_to_int("123"))
print(type(str_to_int("123")))
print(str_to_int("-12332"))
print(type(str_to_int("-12332")))
print(str_to_int("554"))
print(type(str_to_int("554")))


def str_to_int(input_str):

    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int


s = "554"
x = str_to_int(s)
print(x)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))
