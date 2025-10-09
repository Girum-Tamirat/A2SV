# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        def conv(i):
            return chr(ord('a') + i-1)
        res = []
        i = len(s)-1
        while i>=0:
            if s[i] == "#":
                n = int(s[i-2:i])
                res.append(conv(n))
                i-=3
            else:
                res.append(conv(int(s[i])))
                i-=1
        return ''.join(reversed(res))