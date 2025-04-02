# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        mx, i, ac = 1, 0, 0
        for j in range(1, len(s)):
            if s[j] == s[j-1]:
                ac += 1
            while ac > 1:
                if s[i] == s[i+1]:
                    ac -= 1
                i += 1
            mx = max(mx, j - i + 1)
        return mx