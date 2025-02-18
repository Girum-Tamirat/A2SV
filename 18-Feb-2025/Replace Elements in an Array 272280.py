# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {num : index for index, num in enumerate(nums)}
        for x, y in operations:
            index = dic[x]
            nums[index] = y
            dic[y] = index
            del dic[x]
        return nums