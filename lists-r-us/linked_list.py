class ListNode:
    """
    Class for a node in a singly linked list.
    """

    def __init__(self, value, next=None):
    """
    """
    self.value = value
    self.next = next

class LinkedListIterator:
    """
    Iterator for (singly) linked lists.
    """

    def __iter__(node, stop):
        self.current = node
        self.stop = stop #
        return self

    def is_finished(self):
        return self.current is self.stop

    def __next__(self):
        self.current = self.current.next
        if self.is_finished():
            raise StopIteration()
        return self.current.value

class LinkedList:
    """
    Basic implementation of a singly linked list.
    """

    def __init__(self):
        self.head = ListNode(None) #Keep a dummy node to simplify things
        self.head.next = self.head #Use a circular list, i.e. lat node points to first
        self.size=0

    def __iter__(self, position=0):
        return self

    def __next__(self):
        pass

    def insert(value, position=0):
        """
        Inserts the value at the specified position (index).
        """
        pass

    def find(value):
        """
        Returns an iterator starting at the first node containing value.
        """
        current = self.head
        while current.next is not self.head and current.value != value:
            current = current.next
        return LinkedListIterator(current)
