# 设计循环双端队列
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_n = k  # 标记队列最大长度
        self.cur_n = 0  # 标记当前队列长度
        self.queue = [0 for _ in range(k)]  # 队列空间初始化
        self.front, self.rear = 0, 0  # front指向队头元素，rear指向队尾空闲位置

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.cur_n == self.max_n:  # 队满
            return False
        self.front = (self.front - 1) % self.max_n
        self.queue[self.front] = value
        self.cur_n += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.cur_n == self.max_n:  # 队满
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.max_n
        self.cur_n += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.cur_n:  # 队空
            return False
        self.front = (self.front + 1) % self.max_n
        self.cur_n -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.cur_n:  # 队空
            return False
        self.rear = (self.rear - 1) % self.max_n
        self.cur_n -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.cur_n:  # 队空
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.cur_n:  # 队空
            return -1
        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.cur_n

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cur_n == self.max_n
