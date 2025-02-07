# Problem: Find the Maximum Achievable Number - https://leetcode.com/problems/find-the-maximum-achievable-number/description/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = 0
        for _ in range(t):
            num += 1
            x += 1
        x = num + x
        return x

