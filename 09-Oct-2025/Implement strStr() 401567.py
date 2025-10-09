# Problem: Implement strStr() - https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, h: str, n: str) -> int:
        for i in range(len(h)-len(n)+1):
            if h[i:i+len(n)]==n: return i
        return -1
