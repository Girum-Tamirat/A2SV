# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        c, p, l = 0, 1, 0
        for r, num in enumerate(nums):
            p *= num
            while p >= k:
                p //= nums[l]
                l += 1
            c += r-l+1
        return c