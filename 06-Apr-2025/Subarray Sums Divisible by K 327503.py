# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p, r = 0, 0
        mg = [0] * k
        mg[0] = 1
        for num in nums:
            p = (p + num % k + k) % k
            r += mg[p]
            mg[p] += 1
        return r