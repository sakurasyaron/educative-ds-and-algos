class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None  # delete the node to save space
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None  # delete the node to save space

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
            if cur_node is None:
                return
            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n, method):
        if method == 1:
            total_len = self.len_iterative()
            cur = self.head
            while cur:
                if total_len == n:
                    # print(cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return
        elif method == 2:
            p = self.head
            q = self.head
            count = 0
            while q:
                count += 1
                if count >= n:
                    break
                q = q.next
            if not q:
                print(str(n) + " is greater than the number of nodes in the list")
                return
            while p and q.next:
                p = p.next
                q = q.next
            return p.data

    def count_occurrences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev
            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome_1(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome_2(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []
            i = 0
            while q:
                prev.append(q.data)
                q = q.next
                i += 1
            q = prev[i-1]
            count = 1
            while count <= i//2 + 1:
                if prev[-count] != p.data:
                    return False
                p = p.next
                count += 1
        return True

    def is_palindrome(self, method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()

    def move_tail_to_head(self):
        if self.head and self.head.next:
            p = self.head
            prev = None
            while p.next:
                prev = p
                p = p.next
            p.next = self.head
            self.head = p
            prev.next = None

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        sum_llist = LinkedList()
        sum = None
        if not p:
            return llist
        if not q:
            return self
        while p and q:
            total = p.data + q.data + carry
            rem = total % 10
            carry = total // 10
            new_node = Node(rem)
            if not sum:
                sum_llist.head = new_node
                sum = sum_llist.head
            else:
                sum.next = new_node
                sum = sum.next
            p = p.next
            q = q.next
        while p:
            total = p.data + carry
            rem = total % 10
            carry = total // 10
            new_node = Node(rem)
            sum.next = new_node
            sum = sum.next
            p = p.next
        while q:
            total = q.data + carry
            rem = total % 10
            carry = total // 10
            new_node = Node(rem)
            sum.next = new_node
            sum = sum.next
            q = q.next
        if carry:
            new_node = Node(carry)
            sum.next = new_node
            sum = sum.next
        return sum_llist

    def sum_two_lists_2(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist


# llist = LinkedList()
# print("The length of an empty linked list is:")
# print(llist.len_recursive(llist.head))
# llist.append("A")
# llist.append("B")
# llist.print_list()
# print("---------")
# llist.prepend("C")
# llist.print_list()
# print("---------")
# llist.insert_after_node(llist.head.next, "D")
# llist.print_list()
# print("---------")
# llist.delete_node("D")
# llist.print_list()
# print("---------")
# llist.delete_node("E")
# llist.print_list()
# print("---------")
# llist.append("F")
# llist.append("G")
# llist.print_list()
# print("---------")
# llist.delete_node_at_pos(0)
# llist.print_list()
# print("---------")
# llist.delete_node_at_pos(2)
# llist.print_list()
# print("---------")
# print("The length of the linked list calculated recursively is:")
# print(llist.len_recursive(llist.head))
# print("The length of the linked list calculated iteratively is:")
# print(llist.len_iterative())
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# print("Original List")
# llist.print_list()
# print("---------")
# llist.swap_nodes("B", "C")
# print("Swapping nodes B and C that are not head nodes")
# llist.print_list()
# llist.swap_nodes("A", "B")
# print("Swapping nodes A and B where key_1 is head node")
# llist.print_list()
# llist.swap_nodes("D", "B")
# print("Swapping nodes D and B where key_2 is head node")
# llist.print_list()
# llist.swap_nodes("C", "C")
# print("Swapping nodes C and C where both keys are same")
# llist.print_list()
# print("---------")
# llist.reverse_iterative()
# llist.print_list()
# print("---------")
# llist.reverse_recursive()
# llist.print_list()
# llist_1 = LinkedList()
# llist_2 = LinkedList()
#
# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
# llist_1.print_list()
# print("---------")
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
# llist_2.print_list()
# print("---------")
# llist_1.merge_sorted(llist_2)
# llist_1.print_list()
#
# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)
#
# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.append("E")
#
# print(llist.print_nth_from_last(4, 1))
# print(llist.print_nth_from_last(4, 2))

# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
#
# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurrences_iterative(1))
# print(llist_2.count_occurrences_recursive(llist_2.head, 1))
#
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
# llist.rotate(4)
# llist.print_list()

# Example palindromes:
# RACECAR, RADAR
# Example non-palindromes:
# TEST, ABC, HELLO

# llist = LinkedList()
#
# llist_2 = LinkedList()
# llist_2.append("A")
# llist_2.append("B")
# llist_2.append("A")
# llist_2.append("C")
# llist_2.append("A")
#
# print(llist.is_palindrome(1))
# print(llist.is_palindrome(2))
# print(llist.is_palindrome(3))
# print(llist_2.is_palindrome(1))
# print(llist_2.is_palindrome(2))
# print(llist_2.is_palindrome(3))
#
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
#
# llist.move_tail_to_head()
# llist.print_list()

# llist = LinkedList()
# llist.append(8)
# llist.append(2)
# llist.append(9)
#
# llist2 = LinkedList()
# llist2.append(2)
# llist2.append(8)
#
# llist3 = llist.sum_two_lists(llist2)
# llist3.print_list()
# print("---------")
# llist3 = llist.sum_two_lists_2(llist2)
# llist3.print_list()
# 3 6 5
#   4 2
# ------
#
llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
llist3 = llist1.sum_two_lists(llist2)
llist3.print_list()
print("---------")
llist3 = llist1.sum_two_lists_2(llist2)
llist3.print_list()
print("---------")