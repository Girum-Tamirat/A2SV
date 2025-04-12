# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        ans = []
        a = Counter(p)
        for j in range(len(s)):
            win = s[i:i+len(p)]
            c = Counter(win)
            if a == c:
                ans.append(i)
            i += 1
        return ans