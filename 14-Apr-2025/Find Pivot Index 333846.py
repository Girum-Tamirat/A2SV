# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ls = sum(nums[:i])
            rs = sum(nums[i:])-nums[i]
            if ls == rs:
                return i
        return -1