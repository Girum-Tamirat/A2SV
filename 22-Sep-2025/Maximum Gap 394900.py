# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        a = 0
        for i in range(1, n):
            b=nums[i]-nums[i-1]
            a=max(a,b)
        return a
