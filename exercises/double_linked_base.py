class _DoubleLinkedBase:
    """A base class providing a doubly linked list representation.
    This is an important base class!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Use sentinel to streamline operating logic is a great """

    class _Node:
        """ligtweight, nonpublic class for string a doubly linked node"""
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, nxt, element, prev):
            self._element = element
            self._next = nxt
            self._prev = prev

    def __init__(self):
        """create a empty doubly linked node"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header  #
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add an element (e) between two existing nodes and return the new node
        predecessor and successor are the two specified nodes."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """delete nonsentinel node(非哨兵节点) from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = successor
        self._size -= 1
        element = node._element
        node._element = node._prev = node._next = None  # deprecate(弃用) deleted node.
        return element
