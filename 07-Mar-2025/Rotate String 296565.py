# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        r = []
        for i in range(len(s)):
            x = s[0]
            s = s.replace(x,'', 1)
            s= s + x
            r.append(s)
        for j in r:
            if j == goal:
                return True
        return False
        
       