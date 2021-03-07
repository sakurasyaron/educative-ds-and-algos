def int_to_str(input_int):
    if input_int < 0:
        is_neg = True
        input_int *= -1
    else:
        is_neg = False

    output_str = []

    if input_int == 0:
        output_str.append("0")
    else:
        while input_int > 0:
            output_str.append(chr(ord("0") + input_int%10))
            input_int //= 10
        output_str = output_str[::-1]
    output_str = "".join(output_str)
    if is_neg:
        return "-" + output_str
    else:
        return output_str


input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))
#
#
# print(str(123))
# print(type(str(123)))
#
# # Prints 48 which is the Unicode code point of the character '0'
# print(ord('0'))
# # Prints the character '0' as 48 is Unicode code point of the character '0'
# print(chr(ord('0')))
# # Prints 49
# print(ord('0') + 1)
# # Prints 49 which is Unicode code point of the character '1'
# print(ord('1'))
# # Prints the character '2' as 50 is Unicode code point of the character '2'
# # ord('0') + 2  = 48 + 2 = 50
# print(chr(ord('0') + 2))
# # Prints the character '3' as 51 is Unicode code point of the character '3'
# # ord('0') + 3  = 48 + 2 = 51
# print(chr(ord('0') + 3))
