# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        c, m, l = 0, 0, 0
        for num in nums:
            while num in seen:
                c -= nums[l]
                seen.remove(nums[l])
                l += 1
            c += num
            seen.add(num)
            m = max(m, c)
        return m