# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mp = {}
        stc = []
        v = set()
        for i,char in enumerate(s):
            mp[char] = i
        for i, char in enumerate(s):
            if char not in v:
                while stc and stc[-1] > char and mp[stc[-1]] > i:
                    v.remove(stc.pop())
                stc.append(char)
                v.add(char)
        return "".join(stc)