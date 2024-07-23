class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self) -> None:
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.recursive_add(data, self.root)

    def recursive_add(self, data, node):
        if node.left is None:
            node.left = Node(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right = Node(data)
            self.heapify_up(node.right)

        else:
            if self.get_count(node.left) <= self.get_count(node.right):
                self.recursive_add(data, node.left)
            else:
                self.recursive_add(data, node.right)

    def get_count(self, node):
        if not node:
            return 0
        return 1 + self.get_count(node.left) + self.get_count(node.right)

    def heapify_up(self, node):
        while node and node != self.root:
            parent = self.get_parent(node, self.root)
            if parent and parent.data > node.data:
                parent.data, node.data = node.data, parent.data
                node = parent
            else:
                break

    def get_parent(self, node, root):
        if root.left == node or root.right == node:
            return root
        if root.left:
            parent = self.get_parent(node, root.left)
            if parent:
                return parent
        if root.right:
            parent = self.get_parent(node, root.right)
            if parent:
                return parent
        return None

    def extract_min(self):
        if not self.root:
            print("root is none")
            return
        min_val = self.root.data
        last_node_val = self.remove_last_node()
        if last_node_val:
            self.root.data = last_node_val
            self.heapify_down(self.root)
        else:
            self.root = None
        return min_val

    def remove_last_node(self):
        if not self.root:
            return None
        queue = [self.root]
        last_node = None
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            last_node = current
        if last_node:
            parent = self.get_parent(last_node, self.root)
            if parent:
                if parent.left == last_node:
                    parent.left = None
                else:
                    parent.right = None
            return last_node.data
        return None

    def heapify_down(self, node):
        while node:
            small = node
            if node.left and node.left.data < small.data:
                small = node.left
            if node.right and node.right.data < small.data:
                small = node.right
            if small != node:
                small.data, node.data = node.data, small.data
                node = small
            else:
                break


min_heap = MinHeap()
minheap = MinHeap()
minheap.add(10)
minheap.add(7)
minheap.add(6)
minheap.add(5)
minheap.add(4)
print(minheap.extract_min())
print(minheap.extract_min())
print(minheap.extract_min())
