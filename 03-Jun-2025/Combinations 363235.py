# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        coms = []
        def backt(i, com):
            if len(com) == k:
                coms.append(com[:])
                return
            if i >= n:
                return
            com.append(nums[i])
            backt(i+1, com)
            com.pop()
            backt(i+1, com)
        backt(0, [])
        return coms