# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.minstc = []

    def push(self, val: int) -> None:
        self.minstc.append(val)

    def pop(self) -> None:
        self.minstc.pop()

    def top(self) -> int:
        return self.minstc[-1]

    def getMin(self) -> int:
        return min(self.minstc)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()