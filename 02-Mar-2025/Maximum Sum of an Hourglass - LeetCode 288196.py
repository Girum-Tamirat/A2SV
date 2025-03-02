# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ms = 0
        for i in range(m - 2):
            for j in range(n - 2):
                cs = (grid[i][j] + grid[i][j+1] + grid[i][j+2] + 
                     grid[i+1][j+1] + 
                     grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2])
                ms = max(ms, cs)
        return ms
                
