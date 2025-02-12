# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [key for key, value in c.items() if value > len(nums)/3]