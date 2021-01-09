def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


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

def heapsort(tree):
    last_node_index = len(tree) - 1

    for index in range(last_node_index, 0 , -1):
        heapify(tree, index, last_node_index)

    for i in range(last_node_index, 1, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i-1)

# My answer
# def heapsort(tree):
#     tree_size = len(tree)

#     for i in range(1, tree_size):
#         index = tree_size - i
#         heapify(tree, index, tree_size)

#     for i in range(1, tree_size-1):
#         index = tree_size - i
#         swap(tree, 1, index)
#         heapify(tree, 1, len(tree)-i)

# Test code
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]

heapsort(data_to_sort)
print(data_to_sort)