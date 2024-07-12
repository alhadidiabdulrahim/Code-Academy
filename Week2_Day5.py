# -*- coding: utf-8 -*-
"""

Challange of The Day 
---------------------
By Abdulrahim Alhadidi

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(lst):
        linked_list = LinkedList()
        for item in lst:
            linked_list.append(item)
        return linked_list

def add_two_numbers(l1, l2):
    p1, p2 = l1.head, l2.head
    carry = 0
    result_list = LinkedList()

    while p1 or p2 or carry:
        val1 = p1.data if p1 else 0
        val2 = p2.data if p2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        result_list.append(total % 10)

        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    return result_list

l1 = LinkedList.from_list([2, 4, 3]) #[9,9,9,9,9,9,9]
l2 = LinkedList.from_list([5, 6, 4]) #[9,9,9,9]
result = add_two_numbers(l1, l2)

print(result.to_list())
