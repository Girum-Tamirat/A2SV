# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def rec(self, n: int, k: int):
            if n == 1:
                return 0
            el = (2**(n-1))//2
            if k > el:
                return 1 - self.rec(n, k-el)
            return self.rec(n-1, k)
    def kthGrammar(self, n: int, k: int) -> int:
        return self.rec(n, k)
    
        