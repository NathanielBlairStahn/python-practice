"""
Implements a binary search tree with tree node as a separate "inner" class.
Not the best idea...
"""

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def find(self, value, *args):
        """
        Returns the node containing value, and its parent node.
        """
        current, parent = args[0], args[1] if len(args) > 0 else self.root, None

        if current is None or value == current.data:
            #We've found the place where the value is or is supposed to be
            return current, parent
        elif value < current.data:
            #search to the left and pass current node as parent
            return self.find(value, current.left, current)
        elif value > current.data:
            #search to the right and pass current node as parent
            return self.find(value, current.right, current)

    def add(self, value):
        """Adds a value to the tree if it isn't already there.
        Returns True if a new node was created, False if not (value already existed).
        """
        leaf, parent = self.find(value)

        if leaf is not None:
            #Tree already contains value in leaf - do not add duplicate.
            #raise exception? return False? just return?
            return False #value was not added

        new_node = BinaryTreeNode(value)

        if parent is None:
            #tree is empty, add root
            self.root = new_node
        elif value < parent.data:
            parent.left = new_node
        elif value > parent.data:
            parent.right = new_node

        return True #value was added


    # def add(self, value, *args):
    #     current = self.root if len(args) == 0 else args[0]
    #
    #     if current is None:
    #         #current = BinaryTreeNode(data=value)
    #         new_node = BinaryTreeNode(data=value)
    #         if len(args) == 0:
    #             self.root = new_node
    #         elif args[1] == 'left':
    #             args[2].left = new_node
    #         elif args[1] == 'right':
    #             args[2].right = new_node
    #     elif value < current.data:
    #         self.add(value, current.left, 'left', current)
    #     elif value > current.data:
    #         self.add(value, current.right, 'right', current)
    #     else:
    #         pass #value is equal -- throw an error?
