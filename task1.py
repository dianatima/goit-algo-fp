class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# reverse list
def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


# Insertion sort
def sorted_insert(sorted_list, new_node):
    if not sorted_list.head or sorted_list.head.data >= new_node.data:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node


def insertion_sort(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = None
        sorted_insert(sorted_list, current)
        current = next_node
    linked_list.head = sorted_list.head


# merge sorted lists
def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    if current2:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


print("First list")
list1 = LinkedList()
list1.append(5)
list1.append(7)
list1.append(1)
list1.append(4)
list1.append(9)
list1.print_list()

reverse_list(list1)
list1.print_list()

insertion_sort(list1)
list1.print_list()

print("Second list")
list2 = LinkedList()
list2.append(6)
list2.append(2)
list2.append(8)
list2.append(3)
list2.print_list()

reverse_list(list2)
list2.print_list()

insertion_sort(list2)
list2.print_list()

print("Merged list")
merged_list = merge_sorted_lists(list1, list2)
merged_list.print_list()