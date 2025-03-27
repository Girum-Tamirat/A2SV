# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        mx = 0
        for price in prices:
            mn = min(mn, price) 
            mx = max(mx, price - mn)
        return mx