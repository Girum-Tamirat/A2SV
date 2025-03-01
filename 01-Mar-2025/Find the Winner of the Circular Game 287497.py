# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a = 0
        for i in range(1, n + 1):
            a = (a + k) % i
        return a + 1