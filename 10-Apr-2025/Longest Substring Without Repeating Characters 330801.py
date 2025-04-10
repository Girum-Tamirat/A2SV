# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = l = 0
        c = set()
        for j in range(len(s)):
            while s[j] in c:
                c.remove(s[i])
                i += 1
            c.add(s[j])
            l = max(l, j-i+1)
        return l