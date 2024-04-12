class Node:
    def __init__(self, value) -> None:
        self.value = value,
        self.next = None

    def __repr__(self) -> str:
        return f"This Node has value of {self.value} and its next node is {self.next}"

new_node = Node(10)
print(new_node)

# CREATE EMPTY LINKED LIST
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def __repr__(self) -> str:
        llstr = f""

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)

print("head", new_linked_list.head)
print("tail", new_linked_list.tail)
print("head.value",new_linked_list.head.value)
print("tail.value",new_linked_list.tail.value)
print("head.next",new_linked_list.head.next)
print("tail.next",new_linked_list.tail.next)
print("length",new_linked_list.length)

