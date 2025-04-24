# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stc = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stc and temperatures[i] > temperatures[stc[-1]]:
                pi = stc.pop()
                res[pi] = i - pi
            stc.append(i)
        return res