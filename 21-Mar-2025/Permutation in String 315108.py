# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a, b = len(s1), len(s2)
        if a > b:
            return False
        ss1 = sorted(s1)
        for i in range(b - a + 1): 
            if sorted(s2[i:i + a]) == ss1:
                return True 
        return False