# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        b = []
        c = []
        for i in range(n):
            a.append(nums[i])
        for j in range(n, 2*n):
            b.append(nums[j])
        for k in range(n):
            c.append(a[k])
            c.append(b[k])
        return c