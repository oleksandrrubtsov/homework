class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.val:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.val = self._find_min_value(node.right)
            node.right = self._delete_recursive(node.right, node.val)

        return node

    def _find_min_value(self, node):
        min_value = node.val
        while node.left is not None:
            min_value = node.left.val
            node = node.left
        return min_value


binary_tree = BinaryTree()


binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(70)
binary_tree.insert(60)
binary_tree.insert(80)


print("Binary Tree:")
binary_tree._print_tree(binary_tree.root)


binary_tree.delete(20)


print("Binary Tree after deleting 20:")
binary_tree._print_tree(binary_tree.root)