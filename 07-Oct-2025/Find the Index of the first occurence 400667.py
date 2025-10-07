# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, h: str, n: str) -> int:
        for i in range(len(h)-len(n)+1):
            if h[i:i+len(n)]==n: return i
        return -1