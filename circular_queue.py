from ch07.exceptions import Empty


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        def __init__(self, nxt, element):
            self._next = nxt
            self._element = element

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        if self.is_empty:
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty:
            raise Empty("Queue is empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next  # why bypass the oldhead???
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the end of the queue"""
        newest = self._Node(e, None)  # 尾部新增的节点指向None
        if self.is_empty:
            newest._next = newest
        else:
            newest._next = self._tail._next  # 更新“首节点”的previous节点
            self._tail._next = newest  # 旧尾节点指向新增的节点。至此，旧链表与新节点连接成功。
        self._tail = newest  # 新节点成为新的尾节点
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next
