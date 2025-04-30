# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.c = 0
        self.sz = k
        self.i = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.i + self.c) % self.sz] = value
        self.c += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.i = (self.i + 1) % self.sz
        self.c -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.i]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[(self.i + self.c - 1) % self.sz]

    def isEmpty(self) -> bool:
        return self.c == 0

    def isFull(self) -> bool:
        return self.c == self.sz


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()