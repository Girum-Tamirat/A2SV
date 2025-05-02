# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def power(b, e):
            if e == 0:
                return 1
            ans = power(b, e//2)
            ans = (ans * ans) % MOD
            if e%2: ans = (b * ans) % MOD
            return ans
        return (power(5, (n+1)//2) * power(4, n//2)) % MOD