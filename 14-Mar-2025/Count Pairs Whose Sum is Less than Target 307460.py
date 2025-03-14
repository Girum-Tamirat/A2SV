# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    c += 1
        return c