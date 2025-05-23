# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, j in enumerate(s):
            if c[j] == 1:
                return i
        return -1