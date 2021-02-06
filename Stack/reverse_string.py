from stack import Stack


def reverse_string(input_str):
    s = Stack()
    rev_str = ""
    for elem in input_str:
        s.push(elem)
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str


print(reverse_string("Gladiator"))
print(reverse_string("Hello World!"))
print(reverse_string("!aidnI ot emocleW"))