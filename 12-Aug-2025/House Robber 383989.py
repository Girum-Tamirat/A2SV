# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        p2, p1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            c = max(p1, p2 + nums[i])
            p2, p1 = p1, c
        return p1