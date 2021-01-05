def get_left_child_index(complete_binary_tree, index):
    left_child_index = 2 * index

    if len(complete_binary_tree) - 1 < left_child_index:
        return None
    else:
        return left_child_index

def get_right_child_index(complete_binary_tree, index):
    right_child_index = 2 * index + 1

    if len(complete_binary_tree) -1 < right_child_index:
        return None
    else:
        return right_child_index

def get_parent_index(complete_binary_tree, index):
    parent_index = index // 2

    if 0 < parent_index < len(complete_binary_tree):
        return parent_index
    else:
        return None


root_node_index = 1
tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)