class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value


class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_traversal(tree.root)
        elif traversal_type == "reverselevelorder":
            return self.reverse_levelorder_traversal(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_traversal(self, start, traversal=""):
        """Root->Left->Right"""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal=""):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal=""):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_traversal(self, start):
        if not start:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_traversal(self, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size_(self, node):
        if node is None:
            return 0
        left_size = self.size_(node.left)
        right_size = self.size_(node.right)
        return 1 + left_size + right_size

    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

# print(tree.preorder_traversal(tree.root))
# 1-2-4-5-3-6-7-
# print(tree.inorder_traversal(tree.root))
# 4-2-5-1-6-3-7-
# print(tree.postorder_traversal(tree.root))
# 4-5-2-6-7-3-1-
# print(tree.levelorder_traversal(tree.root))
# 1-2-3-4-5-6-7-
# print(tree.reverse_levelorder_traversal(tree.root))
# 4-5-6-7-2-3-1-

# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))
# print(tree.print_tree("levelorder"))
# print(tree.print_tree("reverselevelorder"))

# print(tree.height(tree.root))
print(tree.size_(tree.root))
