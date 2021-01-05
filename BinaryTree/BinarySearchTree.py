def print_inorder(node):
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class Node:
    """Node class for Binary Search Tree"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_sorted_tree(self):
        print_inorder(self.root)

    def insert(self, data):
        iterator = self.root
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        while iterator is not None:
            if new_node.data > iterator.data:
                if iterator.right_child is None:
                    iterator.right_child = new_node
                    new_node.parent = iterator
                    return
                else:
                    iterator = iterator.right_child
            else:
                if iterator.left_child is None:
                    iterator.left_child = new_node
                    new_node.parent = iterator
                    return
                else:
                    iterator = iterator.left_child
        

    # def insert(self, data, old_node): # First trial
        # new_node = Node(data)
        # if old_node is None:
        #     self.root = new_node
        # elif new_node.data > old_node.data:
        #     if old_node.right_child is None:
        #         old_node.right_child = new_node
        #         new_node.parent = old_node
        #     else:
        #         self.insert(data, old_node.right_child)
        # else:
        #     if old_node.left_child is None:
        #         old_node.left_child = new_node
        #         new_node.parent = old_node
        #     else:
        #         self.insert(data, old_node.left_child)






# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# # 이진 탐색 트리 출력
bst.print_sorted_tree()