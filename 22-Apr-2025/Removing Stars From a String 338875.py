# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        l = "".join(s)
        ans = []
        i = 0
        while i < len(l):
            if l[i] != "*":
                ans.append(l[i])
                i += 1
            else:
                ans.pop()
                i += 1
        return "".join(ans)