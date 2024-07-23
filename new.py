# class Node:
#     def __init__(self) -> None:
#         self.children  = {}
#         self.is_end = False

# class Trie:
#     def __init__(self) -> None:
#         self.root = Node()

#     def add(self, word):
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 curr.children[char] = Node()
#             curr = curr.children[char]
#         curr.is_end = True

#     def search(self, word):
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 return False
#             curr = curr.children[char]
#         return curr.is_end

#     def delete(self, word):
#         if not self.search(word):
#             print("Word not found!!")
#             return
#         curr = self.root
#         stack = []

#         for char in word:
#             stack.append(curr)
#             curr = curr.children[char]
#         curr.is_end = False

#         while len(stack) > 0:
#             node = stack.pop()
#             char = word[len(stack)]
#             if not node.children[char].is_end and not node.children[char].children:
#                 del node.children[char]

#     def display(self, depth= 0, node = None):
#         if not node:
#             node = self.root

#         for char, child in node.children.items():
#             end = "END" if child.is_end else ""
#             print(" " * (depth * 2), char, end)
#             self.display(depth+1, child)

#     def suggestions(self, word):
#         def dfs(node, path, result):
#             if node.is_end:
#                 result.append("".join(path))
#             for char , child in node.children.items():
#                 dfs(child, path+[char], result)
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 return []
#             curr = curr.children[char]
#         result = []
#         dfs(curr, list(word), result)
#         return result

# t = Trie()
# t.add("APPLE")
# t.add("APP")
# t.add("APPLICATION")
# t.add("APPAM")
# t.add("APOOPAN")
# t.add("ARANA")
# t.display()
# print(t.suggestions("AR"))


# ========================================================================

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self) -> None:
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        self.recursive_add(data, self.root)

    def recursive_add(self, data, node):
        if node and not node.left:
            node.left = Node(data)
            self.heapify_up(node.left)
        elif node and not node.right:
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
                if parent_node.data > node.data:
                    parent_node.data , node.data = node.data , parent_node.data 
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
            
    def extract_min(self):
        if not self.root:
            print("root is empty!!")
            return
        min_val = self.root.data
        last_node_val = self.remove_lastnode()
        if last_node_val:
            self.root.data = last_node_val
            self.heapify_down(self.root)
        else:
            self.root = None
        return min_val
        
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
                
                
                
            
            
            


# minheap = MinHeap()
# minheap.add(10)
# minheap.add(7)
# minheap.add(6)
# minheap.add(5)
# minheap.add(4)
# print(minheap.extract_min())
# print(minheap.extract_min())
# print(minheap.extract_min())


# arr = [2, 11, 13, 5, 6, 7]

arr = [454,43,212,64,2,56,1,5,3]


sec_small = float('inf')
sec_lar = float('-inf')
small = float('inf')
lar = float('-inf')

for num in arr:
    if num > lar:
        sec_lar = lar
        lar = num
    elif num > sec_lar and num != lar:
        sec_lar = num
    if num < small:
        sec_small = small
        small = num
    elif num < sec_small and num != small:
        sec_small = num
print(sec_lar, sec_small)

def heapify(arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n //2 - 1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

heap_sort(arr)
print(arr)