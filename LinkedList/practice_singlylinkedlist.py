class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def access_at(self, index): # O(n)
        marker = self.head

        for _ in range(index):
            marker = marker.next

        return marker
    
    def search(self, data): # O(n)
        marker = self.head

        while marker is not None:
            if marker.data == data:
                return marker
            marker = marker.next
        return f"{data} does not exist in the linked list."

    def prepend(self, data): # O(1)
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, previous_node, data): # O(n)
        new_node = Node(data)
        
        if previous_node == self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def append(self, data): # O(1)
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self): # O(1)
        if self.head is None:
            return "It's already an empty linked list."
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def delete_after(self, previous_node): # O(n)
        if previous_node.next == self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next

    def __str__(self):
        data_list = []
        
        marker = self.head
        while marker is not None:
            data_list.append(str(marker.data))
            marker = marker.next
        
        return "|".join(data_list)



# Test
linkedlist = SinglyLinkedList()

linkedlist.append(1)
linkedlist.append(2)
print(linkedlist)
print(linkedlist.access_at(1).data)
print(linkedlist.search(1).data)
linkedlist.prepend(0)
print(linkedlist)
linkedlist.append(4)
print(linkedlist)
linkedlist.insert_after(linkedlist.search(2), 3)
print(linkedlist)
linkedlist.pop_left()
print(linkedlist)
linkedlist.delete_after(linkedlist.search(3))
print(linkedlist)