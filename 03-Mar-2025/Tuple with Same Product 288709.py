# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pc = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p = nums[i] * nums[j]
                pc[p] += 1
        for c in pc.values():
            if c > 1:
                res += c * (c -1) // 2
        return res * 8        