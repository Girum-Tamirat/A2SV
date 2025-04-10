# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = []
        piles.sort(reverse=True)
        for i in range(len(piles)//3):
            ans.append(piles[i+i+1])
        return sum(ans)