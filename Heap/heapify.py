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

    # My answer
    # left_child_index = 2 * index
    # right_child_index = 2 * index + 1
    #
    # if tree_size < left_child_index:
    #     pass
    # elif tree_size < right_child_index:
    #     if tree[left_child_index] > tree[index]:
    #         swap(tree, left_child_index, index)
    #         heapify(tree, left_child_index, tree_size)
    # else:
    #     max_index = int
    #     if tree[left_child_index] > tree[index]:
    #         max_index = left_child_index
    #         if tree[right_child_index]> tree[left_child_index]:
    #             max_index = right_child_index
    #     else:
    #         max_index = index
    #         if tree[right_child_index] > tree[index]:
    #             max_index = right_child_index

    #     if max_index != index:
    #         swap(tree, max_index, index)
    #         heapify(tree, max_index, tree_size)



# Test code
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]
heapify(tree, 2, len(tree))
print(tree)