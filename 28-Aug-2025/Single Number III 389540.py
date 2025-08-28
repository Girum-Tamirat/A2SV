# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        u = [num for num, count in c.items() if count == 1]
        return u
