# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        t = sum(nums)
        z = t - x
        if z == 0: return len(nums)
        m, c, i = 0, 0, 0
        for j in range(len(nums)):
            c += nums[j]
            while i < len(nums) and c > z:
                c -= nums[i]
                i += 1
            if c == z:
                m = max(m, j-i+1)
        return len(nums) - m if m != 0 else -1