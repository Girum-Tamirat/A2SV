# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i, j, c = 0, len(nums)-1, 0
        nums.sort()
        while i < j:
            if nums[i] + nums[j] < target:
                c += j - i
                i += 1
            else:
                j -= 1
        return c