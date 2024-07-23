class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self.recursiveadd(data, self.root)

    def recursiveadd(self, data, node):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self.recursiveadd(data, node.left)

    def display(self, depth=0, node=None):
        if not node:
            node = self.root

        print(" " * (depth * 2), node.data)
        if node.left is not None:
            self.display(depth + 1, node.left)
        if node.right is not None:
            self.display(depth + 1, node.right)

    def removenode(self, data):
        if not self.root:
            print("The root is empty!!")
            return
        if self.root:
            if self.root.data == data:
                self.root = None
                return
        self.recursiveremove(data, self.root)

    def recursiveremove(self, data, node):
        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None

        if node.left:
            self.recursiveremove(data, node.left)
        if node.right:
            self.recursiveremove(data, node.right)

    def search(self, data):
        nodefound = self.recursivesearch(data, self.root)
        if nodefound:
            print("True")
        else:
            print("False")

    def recursivesearch(self, data, node):
        if not node or node.data == data:
            return node
        return self.recursivesearch(data, node.left) or self.recursivesearch(
            data, node.right
        )


bt = BinaryTree()
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)
bt.add(6)
bt.add(7)
bt.display()
bt.search(2122)
