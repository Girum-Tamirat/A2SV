# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(numRows):
            r = [1] * (i+1)
            for j in range(1, i):
                r[j] = tri[i - 1][j - 1] + tri[i - 1][j]
            tri.append(r)
        return tri