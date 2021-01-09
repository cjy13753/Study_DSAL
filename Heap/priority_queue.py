def heapify(tree, index, last_node_index):

    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index

    if 0 < left_child_index <= last_node_index and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    if 0 < right_child_index <= last_node_index and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, last_node_index)

def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def reverse_heapify(tree, child_index):
    parent_index = child_index // 2

    if 0 < parent_index < len(tree) and tree[child_index] > tree[parent_index]:
        swap(tree, child_index, parent_index)
        reverse_heapify(tree, parent_index)


class PriorityQueue:
    def __init__(self):
        self.heap = [None]


    def insert(self, data):
        self.heap.append(data)
        new_last_index = len(self.heap) - 1
        reverse_heapify(self.heap, new_last_index)

    def extract_max(self):
        last_node_index = len(self.heap) - 1
        swap(self.heap, 1, last_node_index)
        max_value = self.heap.pop()
        heapify(self.heap, 1, last_node_index-1)
        return max_value

    def __str__(self):
        return str(self.heap)

# Test code for inserting
print('Test code for inserting')
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)
print('correct answer should be [None, 13, 9, 11, 3, 6, 1, 10]')

# Test code for 
print('Test code for extract_max')
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())






# My answer
# def reverse_heapify(tree, child_index):
#     parent_index = child_index // 2

#     if child_index > 1:
#         largest_index = parent_index

#         if tree[child_index] > tree[parent_index]:
#             largest_index = child_index
        
#         if largest_index != parent_index:
#             swap(tree, child_index, parent_index)
#             reverse_heapify(tree, parent_index)

# class PriorityQueue:
#     def __init__(self):
#         self.heap = [None]

#     def insert(self, data):
#         self.heap.append(data)
#         new_last_index = len(self.heap)-1

#         reverse_heapify(self.heap, new_last_index)

#     def __str__(self):
#         return str(self.heap)