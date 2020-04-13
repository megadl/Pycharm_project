class ArrayQueue:
    """This is a FIFO queue,circling, and auto resize when elements of the queue reach the upper limit"""
    CAPACITY = 10
    
    def __init__(self):
        """initiate the FIFO with None."""
        self._size = 0
        self._front = 0
        self._data = [None] * ArrayQueue.CAPACITY  # 使用变量增加可维护性。
    
    def _is_empty(self):
        """if there's no element in the queue, return False"""
        return self._size == 0
    
    def __len__(self):
        """return the number of elements in the queue"""
        return self._size
    
    def dequeue(self):
        """Return and remove(garbage collection) the first element of the queue"""
        if self._is_empty():
            raise Exception("Error! Empty queue!!")
        pop_out = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)  # 循环整个队列，所以应该对队列的长度取模
        self._size -= 1
        return pop_out
    
    def enqueue(self, e):
        """assign element to the last index of the queue."""
        if self._size == len(self._data):  # double the array size
            self.resize(2 * self._size)
        avail = (self._front + self._size) % len(self._data)  # 循环队列使用的索引
        self._data[avail] = e
        self._size += 1
    
    def resize(self, cap):
        """resize to a new list of capacity >=len(self)"""
        old = self._data  # 取出老的队列，将其赋值给变量
        self._data = [None] * cap  # 新的队列容量根据enqueue()内容倍增
        # 进对旧队列中的存在的元素重新赋值给新队列相应位置
        walk = self._front  # 避免影响self._front，因为在其他函数中还有用，在这里不可以随意改变它的值。
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % self._size
        

if __name__ == '__main__':
    """本例程有错误，尝试找出错误之处吧！
    array_ququ.py是正确例程。当然，查阅原版例程也是对的。算法书P158页可参考
    
     """
    import random
    
    aq = ArrayQueue()
    for i in range(25):
        aq.enqueue(random.randint(1, 100))
    print(aq._data)