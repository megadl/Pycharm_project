from ch07.exceptions import Empty


class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage."""

    class _Node:
        """A lightweight, nonpublic class for storing a singly linked list. """
        __slots__ = '_next', '_element'  # streamline memory usage

        def __init__(self, nxt, element):
            """A node contains a node link pointing to the next nod and an element"""
            self._next = nxt
            self._element = element

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def push(self, e):
        """Add an element at the top of the stack"""
        self.head = self._Node(e, self.head)
        self._size += 1

    def top(self):
        if not self._is_empty():
            return self.head._element
        else:
            raise Empty("Stack is empty!!!")

    def pop(self):
        """Remove and return the element from the top of the stack(i.e., LIFO)
        Raise Empty exception if the stack is empty"""
        if self._is_empty():
            raise Empty("Stack is empty!!!")
        answer = self.head._element
        self.head = self.head._next
        self._size -= 1
        return answer


if __name__ == '__main__':
    lk = LinkedStack()
    lk.push(1)
    print(lk)
    lk.top()
    lk.pop()
    for i in range(10, 20):
        lk.push(i)
    print(lk.__len__())
    lk.print()
