class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self) -> None:
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self.recursive_add(data, self.root)

    def recursive_add(self, data, node):
        if not node.left:
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
            parent_node = self.get_parent(node, self.root)
            if parent_node:
                if parent_node.data < node.data:
                    parent_node.data, node.data = node.data, parent_node.data
                    node = parent_node
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

    def extract_max(self):  # Renamed method
        if not self.root:
            print("root is empty!!")
            return None
        max_val = self.root.data
        last_node_val = self.remove_lastnode()
        if last_node_val:
            self.root.data = last_node_val
            self.heapify_down(self.root)
        else:
            self.root = None
        return max_val

    def remove_lastnode(self):
        if not self.root:
            return None
        q = [self.root]
        last_node = None
        while len(q) > 0:
            curr = q.pop(0)
            if curr.left:
                q.append(curr.left)
            if curr.right:  
                q.append(curr.right)
            last_node = curr
        if last_node:
            parent = self.get_parent(last_node, self.root)
            if parent and parent.left == last_node:
                parent.left = None
            elif parent and parent.right == last_node:
                parent.right = None
            return last_node.data
        return None

    def heapify_down(self, node):
        while node:
            large = node
            if node.left and node.left.data > large.data:  # Change < to > for MaxHeap
                large = node.left
            if node.right and node.right.data > large.data:  # Change < to > for MaxHeap
                large = node.right
            if large != node:
                node.data, large.data = large.data, node.data
                node = large
            else:
                break
            
    def print_heap(self):
        if not self.root:
            print("Heap is empty")
            return
        q = [self.root]
        while len(q) > 0:
            curr = q.pop(0)
            print(curr.data, end=" ")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        print()

# Test MaxHeap
maxheap = MaxHeap()
maxheap.add(10)
maxheap.add(7)
maxheap.add(6)
maxheap.add(5)
maxheap.add(4)

# Print the heap
maxheap.print_heap()

print(maxheap.extract_max())
maxheap.print_heap()
print(maxheap.extract_max())
maxheap.print_heap()
print(maxheap.extract_max())
maxheap.print_heap()
print(maxheap.extract_max())
maxheap.print_heap()


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        


# Test the heap sort
arr = [12, 11, 7]
heap_sort(arr)
print("Sorted array is:", arr)