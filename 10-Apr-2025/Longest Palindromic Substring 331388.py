# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(i,j):
            while i >= 0 and j < len(s) and s[i]==s[j]:
                i -= 1
                j += 1
            return s[i + 1 : j]
        l = ""
        for i in range(len(s)):
            o = pal(i, i)
            e = pal(i, i+1)
            if len(o) > len(l):
                l = o
            if len(e) > len(l):
                l = e
        return l