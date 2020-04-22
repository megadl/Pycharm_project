from Pycharm_project.exercises.person_list import PersonList


class PriorityQueueBase:
    """Abstract base class for a priority queue"""
    
    class _Item:
        """lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'
        
        def __init__(self, key, value):
            self._key = key
            self._value = value
        
        def __It__(self, other):
            return self._key < other._key  # return Ture if other's priority is higher than self
    
    def is_empty(self):
        return len(self) == 0


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
    
