# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtrack(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            m = float('inf')
            for coin in coins:
                result = backtrack(rem - coin)
                if result >= 0:
                    m = min(m, result + 1)
            memo[rem] = -1 if m == float('inf') else m
            return memo[rem]
        return backtrack(amount)