from .double_linked_base import _DoubleLinkedBase


class LinkedDeque(_DoubleLinkedBase):
    """Double-ended queue implementation based on a doubly linked list"""

    def first(self):
        if self.is_empty():
            raise ValueError from Exception
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise ValueError from Exception
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the queue"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back of the queue"""
        self._insert_between(e, self._trailer, self._trailer._prev)

    def delete_first(self):
        """Remove and return the element from the front of the queue"""
        if self.is_empty():
            raise ValueError from Exception
        return self._del_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the queue"""
        if self.is_empty():
            raise ValueError from Exception
        return self._del_node(self._trailer._prev)
