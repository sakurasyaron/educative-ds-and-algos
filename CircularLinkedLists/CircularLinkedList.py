class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur = self.head
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        break

    def remove_node(self, node):
        if self.head == node:
            if self.head == self.head.next:
                self.head = None
            else:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    break

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size/2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        split_cllist = CircularLinkedList()
        while cur != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        self.print_list()
        print("--------")
        split_cllist.print_list()

    def josephus_circle(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KILL: " + str(cur.data))
            self.remove_node(cur)
            cur = cur.next

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

from SinglyLinkedLists.LinkedList import LinkedList

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

cllist1 = CircularLinkedList()
print(cllist1.is_circular_linked_list(cllist))
print(cllist1.is_circular_linked_list(llist))
