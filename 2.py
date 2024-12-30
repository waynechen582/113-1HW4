class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def find_and_add_child(self, parent_value, child_value):
        def find(node):
            if not node or node.value == parent_value:
                return node
            return find(node.left if parent_value < node.value else node.right)

        parent = find(self.root)
        if parent:
            if child_value < parent.value:
                parent.left = Node(child_value)
            else:
                parent.right = Node(child_value)
        else:
            print("Parent node not found.")

    def display(self):
        def inorder(node):
            return inorder(node.left) + [node.value] + inorder(node.right) if node else []
        print("In-order Traversal:", inorder(self.root))


# 測試
bst = BinarySearchTree()
for num in [28, 23, 33, 41, 22, 27]:
    bst.insert(num)

bst.display()  # 初始
bst.find_and_add_child(33, 35)  # 覆蓋右節點
bst.display()  # 結果
