



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

    def add_parent(self, node):
        self._parents.insert(node)
        node._children.insert(self)

    def remove_child(self, node):
        self._children.remove(node)
        node._parents.remove(self)

    def remove_parent(self, node):
        self._parents.remove(node)
        node._children.remove(self)

    def parents(self):
        return iter(self._parents)

    def children(self):
        return iter(self._children)

    def num_parents(self):
        """Returns the number of parents (the in-degree) of the node."""
        return len(self._parents)

    def num_children(self):
        """Returns the number of children (the out-degree) of the node."""
        return len(self._children)

class HashDigraphNode:
    def __init__(self, label):
        self.label=label
        self._parents = {}
        self._children = {}

    def __str__(self):
        return f"{{label: {self.label}, parents: { {node.label for node in self.parents()} }, children: { {node.label for node in self.children()} } }}"

    def add_child(self, node):
        self._children[node.label] = node
        node._parents[self.label] = self

    def add_parent(self, node):
        self._parents[node.label] = node
        node._children[self.label] = self

    def remove_child(self, node):
        node._parents.pop(self.label)
        return self._children.pop(node.label)

    def remove_parent(self, node):
        node._children.pop(self.label)
        return self._parents.pop(node.label) #Or use .pop(node.label, None) if we're not sure the node is a parent

    def parents(self):
        return self._parents.values()

    def children(self):
        return self._children.values()

    def num_parents(self):
        """Returns the number of parents (the in-degree) of the node."""
        return len(self._parents)

    def num_children(self):
        """Returns the number of children (the out-degree) of the node."""
        return len(self._children)

class Digraph:
    """Class representing a directed graph in which each node is
    identified by a unique hashable label."""

    def __init__(self, nodes=None):
        #Store the nodes as a dictionary keyed by the nodes' labels.
        if nodes is None:
            self._nodes = {}
        else:
            self._nodes = {node.label: node for node in nodes}

    def __str__(self):
        return "\n".join(str(node) for node in self.nodes())

    def nodes(self):
        """Returns an iterator that iterates through the graph's nodes."""
        return self._nodes.values()

    def edges(self):
        """Returns a generator that generates the graph's edges."""
        return ((parent.label, child.label)
            for parent in self.nodes()
            for child in parent.children())

    # def adjacency_matrix(self):
    #     node_list = list(self.nodes())
    #     n = len(node_list)
    #     matrix = np.zeros((n,n))
    #     for i, node in enumerate(node_list):
    #         if

    def add_node(self, label):
        """Adds an empty node with the given label, or does nothing if there is already
        a node with that label. Returns the (new or existing) node with the given label.
        """
        if label in self._nodes:
            node = self._nodes[label]
        else:
            node = LinkedListDigraphNode(label)
            self._nodes[label] = node
        return node

    def add_edge(self, parent_label, child_label):
        """Add an edge from the node with label 'from_label' to the node with
        label 'to_label', adding the two nodes if necessary. Leaves the graph
        unchanged if the edge already exists.
        """
        parent_node = self.add_node(parent_label)
        child_node = self.add_node(to_label)

        # parent_node = self.nodes[parent_label]
        # child_node = self.nodes[child_label]

        #This funciton will also add parent_node to child's parents
        parent_node.add_child(child_node)


# FUNCTIONS OPERATING ON GRAPHS

def find_childless_node(digraph):
    """Finds and returns a childless node in the digraph,
    or returns None if there are none.
    """
    for node in digraph.nodes():
        if node.num_children() == 0:
            return node
    return None #if none was found
