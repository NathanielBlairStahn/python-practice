"""
Classes implementing binary trees, including binary search trees.
Each "tree" is actually a node representing the subtree rooted at that node.
"""

class BinaryTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(BinaryTree):
    """Class implementing a basic binary search tree."""

    def find_with_parent(self, value, *args):
        """
        Returns the node containing value, and its parent node.

        Parameters
        ----------
        args should be empty if calling from the root. Otherwise, args[0]
        is the subtree to search.
        """
        #args[0] is the subtree to search, which will be passed by the parent node.
        #If no subtree is passed, we are searching from the root, so the subtree is self.
        tree, parent = args[0], self if len(args)>0 else self, None

        if tree is None or value == tree.data:
            return tree, parent
        elif value < self.data:
            return self.find_with_parent(value, self.left)
        else: #if value > self.data:
            return self.find_with_parent(value, self.right)

    def find(self, value):
        """Finds the value in the tree and returns it, or returns None
        if value is not in the tree."""
        node = self.find_with_parent(value)[0]
        return node.data if node is not None else None

    def insert(self, value):
        """Inserts a value into the tree if it's not already there.
        Returns True if a new node was created, False if not (value already existed).
        """
        leaf, parent = self.find_with_parent(value)

        if leaf is not None:
            #Tree already contains value in leaf - do not add duplicate.
            #raise exception? return False? just return?
            return False #value was not added

        if parent is None:
            #tree is empty, add value as root
            self.data = value
        elif value < parent.data:
            parent.left = BinarySearchTree(value)
        else: #if value > parent.data:
            parent.right = BinarySearchTree(value)

        return True #value was added

    def find_min(self):
        """Returns the minimum value in the tree."""
        node = self
        while tree.left is not None:
            node = tree.left
        return node

    def find_max(self):
        """Returns the node of maximum value in the tree."""
        node = self
        while node.right is not None:
            node = node.right
        return node

    def remove(self, value):
        """Removes and returns a value from the tree."""
        node, parent = self.find_with_parent(value)

        if node is None:
            return node.data #item not found - do nothing

        if parent is None: #item is root (node is self) - not sure what to do here...
            data = self.data
            self.data = None
            return data

        data = node.data
        #If node has 2 children, either remove the minimum from the right subtree
        #or remove the maximum from the left subtree, and replace the node's data
        #with this min or max value.
        if node.left is not None and node.right is not None:
            node.data = node.right.remove_min().data
            #or:
            #node.data = node.left.remove_max().data
        elif parent.left is node:
            parent.left = node.right if node.right is not None else node.left
        else: #parent.right is node
            parent.right = node.right if node.right is not None else node.left

        return data


    def remove_min(self):
        node = self
        parent = None
        while node.left is not None:
            parent = node
            node = node.left

        if parent is not None:
            parent.left = node.right

        return node
