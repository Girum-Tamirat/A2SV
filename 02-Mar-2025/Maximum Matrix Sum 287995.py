# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        c = 0
        mn = float('inf')
        tot = 0
        for row in matrix:
            for num in row:
                if num < 0:
                    c += 1
                ab = abs(num)
                tot += ab
                if ab < mn:
                    mn = ab

        if c % 2 == 0:
            return tot
        else:
            return tot - 2*mn
