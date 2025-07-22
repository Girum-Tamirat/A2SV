# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        f = 0
        for i in range(len(nums)):
            if i>f:
                return False
            f = max(f, i+nums[i])
        return True