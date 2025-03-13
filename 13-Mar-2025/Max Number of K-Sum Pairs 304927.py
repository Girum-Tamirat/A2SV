# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = []
        i, j, c = 0, len(nums)-1, 0
        nums.sort()
        while i < j:
            if nums[i] + nums[j] == k:
                c += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return c