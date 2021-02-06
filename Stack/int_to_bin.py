from stack import Stack


def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    s = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2
    binary = ""
    while not s.is_empty():
        binary += str(s.pop())
    return binary


print(convert_int_to_bin(242))
print(convert_int_to_bin(45))
print(convert_int_to_bin(8))
print(convert_int_to_bin(55))
print(convert_int_to_bin(70))
print(convert_int_to_bin(0))

print(int(convert_int_to_bin(56), 2) == 56)
