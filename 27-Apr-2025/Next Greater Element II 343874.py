# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stc = []
        for i in range(len(nums)*2):
            while stc and nums[stc[-1]] < nums[i%len(nums)]:
                ans[stc.pop()] = nums[i%len(nums)]
            stc.append(i%len(nums))
        return ans