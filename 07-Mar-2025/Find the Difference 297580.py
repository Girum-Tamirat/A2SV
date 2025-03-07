# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if t.count(c) > s.count(c):
                return (c)