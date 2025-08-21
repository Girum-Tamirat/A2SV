# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        a = []
        for m in range(2**n):
            s = []
            for i in range(n):
                if m & (1<<i):
                    s.append(nums[i])
            a.append(s)
        return a
            