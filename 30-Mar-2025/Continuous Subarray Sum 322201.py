# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r_i = {0: -1}
        p_s = 0
        for i, num in enumerate(nums):
            p_s += num
            r = p_s % k if k != 0 else p_s
            if r in r_i:
                if i - r_i[r] > 1:
                    return True
            else:
                r_i[r] = i
        return False