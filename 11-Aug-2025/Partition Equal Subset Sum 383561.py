# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0: return False
        t = sum(nums)//2
        dp = [False]*(t+1)
        dp[0]=True
        for num in nums:
            for s in range(t, num-1, -1):
                dp[s]=dp[s] or dp[s-num]
        return dp[t]