# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, k
        cs = sum(nums[:k])
        mx = cs
        for i in range(k, len(nums)):
            cs += nums[i] - nums[i - k]
            mx = max(mx, cs)
        return mx / k