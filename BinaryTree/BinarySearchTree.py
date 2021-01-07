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

    def search(self, data):
        iterator = self.root

        while iterator is not None:
            if data > iterator.data:
                iterator = iterator.right_child
            elif data == iterator.data:
                return iterator
            elif data < iterator.data:
                iterator = iterator.left_child
        return None

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

    def delete(self, data):
        target_node = self.search(data)
        parent_node = target_node.parent

        # Case 1: leaf node
        if target_node.left_child is None and target_node.right_child is None:
            if target_node is self.root:
                self.root = None
            else:
                if target_node is parent_node.right_child:
                    parent_node.right_child = None
                    return target_node.data
                else:
                    parent_node.left_child = None
                    return target_node.data
        
        # Case 2: node with only left child
        elif target_node.right_child is None:
            if target_node is self.root:
                self.root = target_node.left_child
                self.root.parent = None
                return target_node.data
            
            if target_node is parent_node.left_child:
                parent_node.left_child = target_node.left_child
                target_node.left_child.parent = parent_node
                return target_node.data
            
            else:
                parent_node.right_child = target_node.left_child
                target_node.left_child.parent = parent_node
                return target_node.data
        
        # Case 3: node with only right child
        elif target_node.left_child is None and target_node.right_child is not None:
            if target_node is self.root:
                self.root = target_node.right_child
                self.root.parent = None
                return target_node.data
            
            if target_node is parent_node.left_child:
                parent_node.left_child = target_node.right_child
                target_node.right_child.parent = parent_node
                return target_node.data
            
            else:
                parent_node.right_child = target_node.right_child
                target_node.right_child.parent = parent_node
                return target_node.data

        # Case 4: node with both left and right child
        else:
            successor =  self.find_min(target_node.right_child)
            target_node.data = successor.data

            if target_node.right_child is successor:
                target_node.right_child = successor.right_child
            else:
                successor.parent.left_child = successor.right_child
            
            if successor.right_child is not None:
                successor.right_child.parent = successor.parent


    @staticmethod
    def find_min(node):
        iterator = node

        while True:
            if iterator.left_child is None:
                return iterator
            iterator = iterator.left_child

    # Insert - my answer
    # def insert(self, data, old_node): 
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

# Create an empty binary search tree
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

# Search node and print
print('-Search node and print')
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))

# Test find_min static method
print('-Test find_min static method')
print(bst.find_min(bst.root).data)
print(bst.find_min(bst.root.right_child).data)

# Delete leaf node
print('-Delete leaf node')
# print(bst.delete(2))
# print(bst.delete(4))

# Print BST after deletion
print('-Print BST after deletion')
bst.print_sorted_tree()

# Delete node with only one child node
print('-Delete node with only one child')
print(bst.delete(5))
print(bst.delete(9))

# Print BST after deletion
print('-Print BST after deletion of node with only one child node')
bst.print_sorted_tree()

# Delete node with bothe left and right node
print('-Print BST after deletion of node with both left and right child')
bst = BinarySearchTree()

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

bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()