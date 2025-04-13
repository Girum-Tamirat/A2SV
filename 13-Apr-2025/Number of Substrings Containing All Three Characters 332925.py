# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lp = [-1] * 3
        tot = 0
        for p in range(len(s)):
            lp[ord(s[p]) - ord("a")] = p
            tot += 1 + min(lp)
        return tot