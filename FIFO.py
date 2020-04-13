from ch06.exceptions import Empty


class ArrayStack:
    CAPACITY = 10

    def __init__(self):
        self._front = 0  # first element index in stack
        self._size = 0
        self._data = [None] * ArrayStack.CAPACITY

    def _is_empty(self):
        return self._size == 0

    def __str__(self):
        return str(self._data)

    def dequeue(self):
        """This function is used to return and remove the first element of the queue"""
        if self._is_empty():
            raise Empty("Queue is empty!!!")
        vail = self._data[self._front]
        self._data[self._front] = None  # remove the first element
        self._front = (self._front + 1) % len(self._data)  # 循环列表，需要取余(remainder)，求值新的首元素索引。
        self._size -= 1
        return vail

    def enqueue(self, e):
        """append element at the end of the cyclic queue, if self._size==len(self._data), double the size of the queue"""
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        # resize之后需要把原队列中的元素原封不动装进新的倍增后的队列里，索引和数值都不能变化！！！！！
        # resize部分的数据迁移功能不是通用功能，只有resize发生时此功能才会启用，所以不要把这个部分代码放在enqueue函数中。
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        # 数据迁移的索引从就队列的self._front开始。
        for i in range(len(old)):
            self._data[walk] = old[i]
            walk = (walk + 1) % self._size  # 这里可以对self._size取余，因为这里self._size肯定等于old队列长度，满足循环要求
        # 扩展队列完成后，必须对首元素索引进行置零。不然扩展后的队列新增元素时就会跳索引，加入self._front==2,扩展完成后使用
        # self.queue(e)，则e的索引avail等于(2+self._size) % len(self._data),中间跳了2个索引。
        self._front = 0


if __name__ == '__main__':
    aq = ArrayStack()
    [aq.enqueue(i) for i in range(10)]
    print(aq)
    for i in range(10):
        aq.dequeue()
        aq.dequeue()
        aq.dequeue()
        aq.dequeue()
        aq.enqueue(20)
    print(aq)
