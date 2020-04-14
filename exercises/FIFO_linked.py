from ch07.exceptions import Empty


class LinkedQueue:
    """FIFO queue linked with a singly linked list for storage"""
    __slots__ = '_element', '_next'

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""

        def __init__(self, nxt, element):
            self._next = nxt
            self._element = element

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return Empty("Queue is empty!!")
        return self.head._element

    def dequeue(self):
        if self.is_empty():
            return Empty("Queue is empty!!")
        answer = self.head._element
        self.head = self.head._next
        self._size -= 1
        # 队列中的元素被dequeue完，队列成为一个空队列时
        if self.is_empty():
            self._tail = None
        return answer

    # 增加链表节点两步骤：1、旧尾部节点指向新增加元素节点 2、新增加元素节点指向尾部空节点None
    def enqueue(self, e):
        newest = self._Node(e, None)  # As a new tail, the newest node points to None.
        if self.is_empty():  # special case: the previous queue is empty.
            self._head = newest
        else:
            self._tail._next = newest  # the old tail should now point to the newest node
        self._tail = newest  # 不要忘记把新的tail赋值为newest
        self._size += 1
