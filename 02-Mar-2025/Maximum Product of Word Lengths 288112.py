# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bm = [0] * n
        ls = [len(word) for word in words]
        for i, word in enumerate(words):
            for char in word:
                bm[i] |= (1 << (ord(char) - ord('a')))
        mp = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bm[i] & bm[j] == 0:
                    mp = max(mp, ls[i] * ls[j])
        return mp