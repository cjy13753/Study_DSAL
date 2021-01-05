from LinkedList import LinkedList


class Node:
    """Doubly Linked List Node"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Doubly Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    def access_at(self, index): # O(n)
        """Access Operation"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def search(self, data): # O(n)
        """Search Operation"""
        iterator = self.head
        
        while iterator is not None:
            if iterator.data == data:
                return iterator.data
            else:
                iterator = iterator.next
        return "No nodes contain {}".format(data)

    def prepend(self, data):
        """Prepend Operation"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_after(self, previous_node, data):
        """Insert_after opeartion"""
        new_node = Node(data)

        if previous_node is self.tail:
            previous_node.next = new_node
            new_node.prev = previous_node
            self.tail = new_node
        else:
            previous_node.next.prev = new_node
            new_node.next = previous_node.next
            previous_node.next = new_node
            new_node.prev = previous_node

    def append(self, data):
        """Append Operation"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        """Delete Operation"""
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node_to_delete:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail is node_to_delete:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        return node_to_delete.data
            

    
    def __str__(self):
        """Traverse Operation"""
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str

# Initializing a new Doubly Linked List
my_list = DoublyLinkedList()

# Testing append opeartion
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

# Testing insert_after operation
my_list.insert_after(my_list.access_at(4), 5)
print(my_list)
print(my_list.tail.data)
my_list.insert_after(my_list.access_at(3), 3)
print(my_list)
my_list.insert_after(my_list.access_at(2), 2)
print(my_list)

# Testing prepend operation
my_list = LinkedList()

my_list.prepend(11)
my_list.prepend(7)
my_list.prepend(5)
my_list.prepend(3)
my_list.prepend(2)

print(my_list)
print(my_list.head.data)
print(my_list.tail.data)

# Testing delete operation
my_list = DoublyLinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

node_at_index_2 = my_list.access_at(2)
my_list.delete(node_at_index_2)
print(my_list)

head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

last_node = my_list.head
my_list.delete(last_node)
print(my_list)