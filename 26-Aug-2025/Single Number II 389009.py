# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        u = [num for num, count in c.items() if count == 1]
        return u[0]