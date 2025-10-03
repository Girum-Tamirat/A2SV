# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        a = 0
        for i in range(len(nums)):
            if nums[i]==0:
                c=0
            if nums[i]==1:
                c+=1
                a=max(a,c)
        return a