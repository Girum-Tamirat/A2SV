# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = float('-inf') 
        for i in reversed(range(len(nums))):
            if nums[i] < second:
                return True 
            while stack and nums[i] > stack[-1]:
                second = stack.pop() 
            stack.append(nums[i])
        return False
