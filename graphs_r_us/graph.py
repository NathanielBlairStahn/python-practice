



class DigraphNode:
    def __init__(self, label):
        self.label=label
        self.first_parent = None
        self.first_child = None
        self.next_node = None

    def add_child(label):
        if self.first_child is None:
            self.first_child = DigraphNode(label)
        else:
            new_node = DigraphNode(label)
            new_node.next_node = self.first_child.next_node
            self.first_child.next_node = new_node


class LinkedListDigraphNode:
    def __init__(self, label):
        self.label=label
        self._parents = LinkedList()
        self._children = LinkedList()

    def __str__(self):
        return f"{{label: {self.label}, parents: { {node.label for node in self.parents()} }, children: { {node.label for node in self.children()} } }}"

    def add_child(node):
        self._children.insert(node)
        node._parents.insert(self)

    def remove_parent(self, node):
        self._parents.remove(node)
        node._children.remove(self)

    def parents(self):
        return iter(self._parents)

    def children(self):
        return iter(self._children)

class HashDigraphNode:
    def __init__(self, label):
        self.label=label
        self._parents = {}
        self._children = {}

    def __str__(self):
        return f"{{label: {self.label}, parents: { {node.label for node in self.parents()} }, children: { {node.label for node in self.children()} } }}"

    def add_child(node):
        self._children[node.label] = node
        node._parents[self.label] = self

    def remove_parent(self, node):
        del self._parents[node.label] #Or use .pop() if we're not sure the node is a parent
        del node._children[self.label]

    def parents(self):
        return self._parents.values()

    def children(self):
        return self._children.values()

class Digraph:
    def __init__(self, nodes=None):
        #Store the nodes as a dictionary keyed by the nodes' labels.
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = {node.label: node for node in nodes}
