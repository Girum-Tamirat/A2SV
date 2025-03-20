# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, cs, ml = 0, 0, float('inf')
        for j in range(len(nums)):
            cs += nums[j]
            while cs >= target:
                ml = min(ml, j-i+1)
                cs -= nums[i]
                i += 1
        return ml if ml != float('inf') else 0
                    