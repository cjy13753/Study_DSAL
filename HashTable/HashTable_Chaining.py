class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search_with_key(self, key):
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator
            
            iterator = iterator.next

        return None
    
    def append(self, key, value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        res_str = ""

        iterator = self.head

        while iterator is not None:
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str

class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [DoublyLinkedList() for _ in range(self._capacity)]

    def _hash_function(self, key):
        """
        Method that uses the division method on the given key to return the hashed value
        Warning: key must be a static type
        """
        return hash(key) % self._capacity

    def search(self, key):
        existing_node = self._look_up_node(key)
        
        if existing_node is not None:
            return existing_node.value
        return None

    def insert(self, key, value):
        existing_node = self._look_up_node(key)
        
        if existing_node is not None:
            existing_node.value = value
        else:
            doubly_linked_list = self._get_doubly_linked_list_for_key(key)
            doubly_linked_list.append(key, value)

    def delete(self, key):
        existing_node = self._look_up_node(key)
        if existing_node is not None:
            doubly_linked_list = self._get_doubly_linked_list_for_key(key)
            doubly_linked_list.delete(existing_node)

    def _get_doubly_linked_list_for_key(self, key):
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]

    def _look_up_node(self, key):
        doubly_linked_list = self._get_doubly_linked_list_for_key(key)
        return doubly_linked_list.search_with_key(key)


    def __str__(self):
        res_str = ""

        for doubly_linked_list in self._table:
            res_str += str(doubly_linked_list)
        
        return res_str[:-1]


# Initializing a hash table
test_scores = HashTable(50)  

# Testing insert operation
test_scores.insert("A", 85)
test_scores.insert("B", 90)
test_scores.insert("C", 87)
test_scores.insert("D", 99)
test_scores.insert("E", 88)
test_scores.insert("F", 97)
test_scores.insert("G", 90)

print(test_scores)

# Testing search opeartion
print(test_scores.search("A"))
print(test_scores.search("G"))
print(test_scores.search("B"))

# Testing insert operation
test_scores.insert("A", 10)
test_scores.insert("G", 20)
test_scores.insert("B", 30)

print(test_scores)

# Testing delete Opeartion
test_scores.delete("F")
test_scores.delete("D")
test_scores.delete("A")
test_scores.delete("E")
test_scores.delete("C")

print(test_scores)