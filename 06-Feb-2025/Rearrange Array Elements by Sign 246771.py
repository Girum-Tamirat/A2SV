# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        ans = []
        for num in nums:
            if num >= 0:
                p.append(num)
            elif num < 0:
                n.append(num)
        for i in range(len(p)):
            ans.append(p[i])
            ans.append(n[i])
        return ans