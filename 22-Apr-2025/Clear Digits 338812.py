# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        dig = "".join([char for char in s if char.isdigit()])
        alp = "".join([char for char in s if char.isalpha()])
        ans = []
        i = 0
        while i < len(s):
            if s[i] not in dig:
                ans.append(s[i])
                i += 1
            else:
                ans.pop()
                i += 1
        return "".join(ans)
