# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uni = sorted(set(nums), reverse=True) 
        return uni[2] if len(uni) >= 3 else uni[0] 