from .person_list import PersonList


class PriorityQueueBase:
    """Abstract base class for a priority queue"""

    class _Item:
        """lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __It__(self, other):
            return self._key < other._key  # return True if other's priority is higher than self

    def is_empty(self):  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def __len__(self):
        """Return the number of items in the priority queue."""
        raise NotImplementedError('must be implemented by subclass')

    def add(self, key, value):
        """Add a key-value pair."""
        raise NotImplementedError('must be implemented by subclass')

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list.
    未排序列表实现的优先级队列"""

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise ValueError("queue is empty!")
        small = self._data.first()  # 初始化small和walk的值，walk应为small随后的值
        walk = self._data.after(small)
        while walk is not None:
            if walk.element < small.element():
                small = walk  # 对列表内的元素按照大小进行排序，较小值赋值给中间变量walk，直到walk值为最小，最后small将是最小值
            walk = self._data.after(walk)  # while单次循环后，初始化时的walk值将变成small值，walk顺位后移。最终walk==None，停止while
        return small  # 返回整个while循环找到的最小值

    def __init__(self):
        self._data = PersonList()  # self._data实际上都是位置信息ADT

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair, O(1)"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key, O(n)"""
        p = self._find_min()  # 含有最小元素的position
        item = p.element()
        return (item._key, item._value)  # return (k, v) tuple

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key, O(n)"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list"""

    def __init__(self):
        self._data = PersonList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):  # 由于需要插入排序，所以导致增加一个position的时间复杂度O（n）
        """Add a key-value pair using insertion sort, O(n)"""
        newest = self._Item(key, value)  # 初始化newest和walk，walk时中间变量，用于存储遍历时的临时最小值
        walk = self._data.last()
        while walk is not None and newest < walk.element():  # 若中间变量walk的值比newest大，则继续执行while
            walk = self._data.before(walk)  # walk在队列中前进，直到walk的值比newest小
        if walk is None:
            self._data.add_first(walk)  # 若优先级队列的最后一个position时None（队列空），则直接把newest放进队列中
        else:
            self._data.add_after(walk, newest)  # 把拥有更小元素的newest放在walk之后的位置。

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key, O(1)"""
        if self.is_empty():
            raise ValueError('PriorityQueue is emtpy')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key, O(1)"""
        if self.is_empty():
            raise ValueError('PriorityQueue is emtpy')
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""

    # -----------------------nonpublic behavior------------------------------------
    def _parent(self, j):
        """j is the index"""
        return (j - 1) // 2

    def _left(self, j):  # p = 2 * f(q) + 1
        return 2 * j + 1

    def _right(self, j):  # p = 2 * f(q) + 2
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """swap the elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._parent(j):
            self._swap(j, parent)  # 在堆heap中交换j和parent两个position
            self._upheap(parent)  # recur at position of parent, parent和parent的self._parent(parent)

    def _downheap(self, j):
        """对新root重新排序，新root与左右孩子相比较所存储的元素值，若root值大于孩子节点元素值，则与之交换位置，递归执行"""
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[left] > self._data[right]:
                    small_child = right  # find the real small_child
            if self._data[j] < self._data[small_child]:  # compare elements stored at position j and small_child
                self._swap(j, small_child)  # move down the smaller one
                self._downheap(small_child)  # recur at position of small child

    # -------------------public methods-------------------------------------------------------------------------
    def __init__(self):
        """Create an empty priority queue"""
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue at the end of the priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)  # 在基于数组的堆实现中，元素索引范围是(0, n-1),因为在最底层最右侧加一个值，也就是最后一个值，这个值得索引肯定是n-1

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key.
        Raise Empty exception if empty"""
        if self.is_emtpy():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove (k,v) tuple with the minimum key.
        Raise Empty exception if empty"""
        if self.is_emtpy():
            raise ValueError('Priority queue is empty')
        self._swap(0, len(self._data)-1)  # 删除顶部最小的值后把该位置与优先级队列最后位置(索引为n-1)调换
        # 由于调换后可能破坏Heap-Order，因此需要调用downheap()方法对优先极队列重新进行排序
        item = self._data.pop()
        self._downheap(0)  # 堆向下冒泡，重新排序。
        return (item._key, item._value)

