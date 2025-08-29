# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold = -prices[0]  
        sold = 0 
        rest = 0  
        for i in range(1, n):
            ph, ps, pr = hold, sold, rest
            hold = max(ph, pr - prices[i]) 
            sold = ph + prices[i]  
            rest = max(pr, ps)    
        return max(sold, rest)