# Tree concepts

"""
Trees are used to represent hierarchical data.

Root: The top node in a tree.

Parent: The node directly connected above a node.

Child: The node directly connected below a node.

Leaf: A node with no children.

Subtree: A tree formed by a node and its descendants.

Height: The length of the longest path from a node to a leaf.

--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------


General Tree : A tree where each node can have any number of children.

Example: The directory structure of a file system where folders can have many subfolders and files.

--------------------------------------------------------------------------------------

Binary Tree : A tree where each node has at most two children.

Example : The organizational structure of a small company where each manager has at most two subordinates.

--------------------------------------------------------------------------------------

Binary Search Tree (BST): A binary tree where the left child contains only nodes with values less than the parent node,
and the right child contains only nodes with values greater than the parent node. 
            
Example : A phone book where names are stored such that you can quickly search for a specific name.

--------------------------------------------------------------------------------------

Balanced Tree : A binary tree where the height difference between the left and right subtrees of any node is at most one.
Example : AVL Tree

--------------------------------------------------------------------------------------

AVL Tree : A self-balancing BST where the height difference between the left and right subtrees of any node is at most one.

--------------------------------------------------------------------------------------

Complete Binary Tree : A binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
Example: A binary heap.

--------------------------------------------------------------------------------------

Perfect Binary Tree : A binary tree in which all internal nodes have exactly two children and all leaf nodes are at the same level.
Example: The structure of a full binary tournament bracket.

--------------------------------------------------------------------------------------

Full Binary Tree : A binary tree in which every node has either 0 or 2 children.
Example: A tree representation of mathematical expressions

--------------------------------------------------------------------------------------

Degenerate (or Pathological) Tree : A tree where each parent node has only one child. This makes the tree essentially a linked list.
Example: A skewed tree where elements are inserted in ascending or descending order.

--------------------------------------------------------------------------------------

B-Tree : A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.
It is commonly used in databases and file systems.
Example: The indexing mechanism used in many database management systems.

--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------




"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentdata=None):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
            return
        parentnode = self.findparent(parentdata, self.root)
        if parentnode:
            parentnode.children.append(node)
            return
        print("Node does not found!!")

    def findparent(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            nodefound = self.findparent(data, child)
            if nodefound:
                return nodefound
        return None

    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        if not node:
            print("Tree is empty!!")
            return
        print(" " * (depth * 2), node.data)
        for child in node.children:
            self.display(depth + 1, child)

    def remove(self, data):
        if self.root is None:
            print("The root is empty!!")
            return
        if self.root.data == data:
            self.root = None
            return "The tree has been terminated!!"

        parentnode = self.findparentnode(data, self.root)
        if parentnode:
            for child in parentnode.children:
                if child.data == data:
                    parentnode.children.remove(child)
                    return
                print("Node with the given data does not exits!!")

    def findparentnode(self, data, node):
        for child in node.children:
            if child.data == data:
                return node
            nodefound = self.findparentnode(data, child)
            if nodefound:
                return nodefound
        return None


tree = Tree()
tree.add(1)
tree.add(2, 1)
tree.add(3, 1)
tree.add(4, 1)
tree.add(5, 2)
tree.add(6, 2)
tree.add(7, 3)
tree.add(8, 3)
tree.add(9, 4)
tree.add(10, 4)
tree.display()
tree.remove(5)
tree.display()
