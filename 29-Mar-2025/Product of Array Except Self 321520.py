# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [math.prod(nums)] * n
        for i in range(n):
            if nums[i] != 0:
                ans[i] //= nums[i]
            else:
                ans[i] = math.prod(nums[:i] + nums[i+1:])
        return ans