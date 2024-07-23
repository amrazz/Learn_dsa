"""
DFS :- Depth first search

1) in order :- Left, current, right
2) pre order :- current, left, right
3) post order :- Left, right, current

"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.recursive_add(data, self.root)

    def recursive_add(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self.recursive_add(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = Node(data)
            else:
                self.recursive_add(data, node.right)

    def display(self):
        result = []
        self.in_order(self.root, result)
        print(result)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def in_order(self, node, result):
        if not node:
            return None
        else:
            self.in_order(node.left, result)
            result.append(node.data)
            self.in_order(node.right, result)
            
            
    def pre_order(self, node, result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)

    def post_order(self, node, result):
        if not node:
            return None
        else:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.data)

    def remove(self, data):
        self.root = self.delete_node(data, self.root)

    def delete_node(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self.delete_node(data, node.left)
        elif data > node.data:
            node.right = self.delete_node(data, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self.find_min(node.right)
            node.data = min_node.data
            node.right = self.delete_node(min_node.data, node.right)
        return node

    def search(self, data):
        node = self.recursive_search(data, self.root)
        if node:
            print("True")
        else:
            print("False")

    def recursive_search(self, data, node):
        if node and node.data == data:
            return node
        elif data < node.data:
            return self.recursive_search(data, node.left)
        elif data > node.data:
            return self.recursive_search(data, node.right)

    def secondsmallandlar(self):
        if not self.root:
            print("The root is empty!!")
            return

        result = []
        self.in_order(self.root, result)

        if len(result) <= 2:
            print("THE element is not enought!!")
            return
        else:
            sec_small = result[1]
            sec_lar = result[-2]
            return sec_small + sec_lar

    def valid(self):
        if not self.root:
            print("Root is emoty!!")
            return False
        return self.valid_search(self.root, float("-inf"), float("inf"))

    def valid_search(self, node, min, max):
        if node is None:
            return True
        if not (min < node.data < max):
            return False

        return self.valid_search(node.left, min, node.data) and self.valid_search(
            node.right, node.data, max)

    def closest(self, target):
        if not self.root:
            return None
        closest = self.root.data
        curr = self.root

        while curr is not None:
            if abs(curr.data - target) < abs(closest - target):
                closest = curr.data

            if target < curr.data:
                curr = curr.left
            elif target > curr.data:
                curr = curr.right
            else:
                break
        return closest

    def find_min(self, node=None):
        if not node:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def find_max(self, node=None):
        if not node:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def second_min(self):
        curr = self.root
        prev = None
        while curr.left:
            prev = curr
            curr = curr.left

        if curr.right:
            return self.find_min(curr.right)
        else:
            return prev.data

    def second_max(self):
        curr = self.root
        prev = None
        while curr.right:
            prev = curr
            curr = curr.right

        if curr.left:
            return self.find_max(curr.left)
        else:
            return prev.data


bt = BST()
bt.add(2)
bt.add(9)
bt.add(11)
bt.add(50)
bt.add(30)
bt.add(150)
print(bt.valid())
# bt.display()

# print(f"Closest value to 100: {bt.closest(100)}")
# print(f"Closest value to 47: {bt.closest(47)}")
# print(f"Closest value to 60: {bt.closest(60)}")
# print(f"Closest value to 160: {bt.closest(160)}")
# print(bt.find_min())
# print(bt.find_max())
# print(bt.second_min())
# print(bt.second_max())
