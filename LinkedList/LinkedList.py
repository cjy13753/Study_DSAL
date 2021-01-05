# Implementation of Linked List
class Node:
    """Node class for Linked List"""

    def __init__(self, data):
        self.data = data # data that the node stores
        self.next = None # reference to the next node


class LinkedList:
    """Linked List Class"""
    
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
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            

    def insert_after(self, previous_node, data):
        """Insert Opeartion"""
        new_node = Node(data)

        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node       
    
    def append(self, data):
        """Append Operation"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_after(self, previous_node):
        """Delete Operation"""
        data = previous_node.next.data
        
        if previous_node.next == self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next

        return data

    def popleft(self):
        """Popleft operation"""
        if self.tail is not None:
            if self.tail != self.head:
                data = self.head.data
                self.head = self.head.next
                return data
            else:
                data = self.head.data
                self.head = None
                self.tail = None
                return data
        else:
            return None
    
    def __str__(self):
        """Traverse Operation"""
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str


# Initializing a new LinkedList
my_list = LinkedList()

# Testing append operation
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

# Testing access operation
print(my_list.access_at(0).data)

# Testing search operation
print(my_list.search(2))
print(my_list.search(11))
print(my_list.search(6))

# Testing insert_after operation
node_at_2 = my_list.access_at(2)
my_list.insert_after(node_at_2, 6)
print(my_list)

head_node = my_list.head
my_list.insert_after(head_node, 9)
print(my_list)

# Testing prepend operation
my_list.prepend(1)
print(my_list)

new_list = LinkedList()
new_list.prepend(1)
print(new_list)

# Testing delete_after opeartion
node_at_2 = my_list.access_at(2)
my_list.delete_after(node_at_2)
print(my_list)

node_at_5 = my_list.access_at(5)
print(my_list.delete_after(node_at_5))
print(my_list)

#Testing popleft operation
print(my_list.popleft())
print(my_list)
new_list = LinkedList()
print(new_list.popleft())