# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, prev):
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                num = int(s[i:j])
                if prev - num == 1 and dfs(j, num):
                    return True
            return False
        for i in range(1, len(s)):
            first = int(s[:i])
            if dfs(i, first):
                return True
        return False
