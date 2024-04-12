class Node:
    def __init__(self, value) -> None:
        self.value = value,
        self.next = None

new_node = Node(10)
print(new_node)

# CREATE EMPTY LINKED LIST
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
#         self.length = 0

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list.length)