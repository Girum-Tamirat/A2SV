# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = 0
        nums.sort(reverse=True)
        p = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == p:
                continue
            if nums[i] < p:
                c += i
            p = nums[i]
        return c