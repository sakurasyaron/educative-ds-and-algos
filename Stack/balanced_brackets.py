from stack import Stack


def is_match(p1, p2):
    if p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    for paren in paren_string:
        if paren in "[{(":
            s.push(paren)
        else:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    return False
    if s.is_empty():
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))

print("String : [{][}] Balanced or not?")
print(is_paren_balanced("[{][}]"))