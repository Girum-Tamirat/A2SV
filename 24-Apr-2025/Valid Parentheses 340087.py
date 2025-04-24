# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stc = []
        brc = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in brc.values():
                stc.append(i)
            elif i in brc.keys():
                if not stc or brc[i] != stc.pop():
                    return False
        return not stc
