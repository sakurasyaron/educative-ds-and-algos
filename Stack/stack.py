class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push("A")
    stack.push("B")
    print(stack.get_stack())
    stack.push("C")
    print(stack.get_stack())
    print(stack.is_empty())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())