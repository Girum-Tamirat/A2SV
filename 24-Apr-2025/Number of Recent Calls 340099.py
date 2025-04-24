# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.recentCounter = deque()

    def ping(self, t: int) -> int:
        self.recentCounter.append(t)
        while self.recentCounter and self.recentCounter[0] < t - 3000:
            self.recentCounter.popleft()
        return len(self.recentCounter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)