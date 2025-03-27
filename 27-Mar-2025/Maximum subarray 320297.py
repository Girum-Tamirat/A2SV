# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float('-inf')
        c = 0
        for num in nums:
            c = max(num, c+num)
            mx = max(c, mx)
        return mx