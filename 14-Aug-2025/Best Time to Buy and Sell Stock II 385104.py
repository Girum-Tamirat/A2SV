# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                p+=prices[i+1]-prices[i]
        return p