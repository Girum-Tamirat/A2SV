# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, res = len(grid), []
        for i in range(1, n - 1):
            tr = []
            for j in range(1, n - 1):
                temp = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])
                tr.append(temp)
            res.append(tr)
        return res