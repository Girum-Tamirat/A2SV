# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:  
        c = 0     
        for i in range(len(nums)):
            cs = nums[i]
            for j in range(i, len(nums)):
                cs = lcm(cs, nums[j])
                if cs==k:
                    c+=1
                elif cs>k: break
        return c