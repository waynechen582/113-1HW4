class BinarySearchTree:
    def __init__(self, size):
        self.tree = [None] * size

    def insert(self, value, index=1):
        if index >= len(self.tree):
            return
        if self.tree[index] is None:
            self.tree[index] = value
        elif value < self.tree[index]:
            self.insert(value, 2 * index)  # 左
        else:
            self.insert(value, 2 * index + 1)  # 右

    def display(self):
        print("Binary Search Tree as Array:")
        print(self.tree)

# 測試
bst = BinarySearchTree(15)
data = [28, 23, 33, 41, 22, 27]
for num in data:
    bst.insert(num)
bst.display()
