def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


p = "Was it a cat I saw?"
print(is_palindrome(p))

# Solution uses extra space proportional to size of string "s"
new_s = ''.join([i for i in p if i.isalnum()]).replace(" ", "").lower()
print(new_s == new_s[::-1])
