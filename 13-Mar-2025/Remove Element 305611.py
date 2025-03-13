# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        nums.sort()
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                nums.pop()
                j -= 1
            else:
                i += 1