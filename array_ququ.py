class ArrayQueue:
    CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.CAPACITY
        self._size = 0
        self._front = 0
        
    def _is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size
    
    def capacity(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)
    
    def dequeue(self):
        """Return and remove the first element of the queue"""
        if self._is_empty():
            raise Exception("ArrayQueue is empty!!!")
        queue_head = self._data[self._front]  # 取出列首元素
        self._data[self._front] = None  # 列首垃圾回收
        self._front = (self._front + 1) % len(self._data)  # 循环列表，重置self._front的值
        self._size -= 1
        return queue_head
        
    def enqueue(self, e):
        if self._size == len(self._data):  # 使用动态数组方式扩展队列，倍增
            self.resize(2 * self._size)
        index = (self._front + self._size) % len(self._data)
        self._data[index] = e
        self._size += 1
        
    def resize(self, cap):
        """create a new queue which is two times larger than the old one."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % self._size
        self._front = 0  # 本函数内self._front 置零非常重要！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！


if __name__ == '__main__':
    aq = ArrayQueue()
    aq.enqueue("A")
    aq.enqueue("B")
    aq.enqueue("C")
    aq.dequeue()
    aq.dequeue()
    
    [aq.enqueue(i) for i in range(199)]
    print(aq, aq.__len__(), aq.capacity(), sep='\n')
    for i in range(103):
        aq.dequeue()
    print(aq, aq.__len__(), aq.capacity(), sep='\n')