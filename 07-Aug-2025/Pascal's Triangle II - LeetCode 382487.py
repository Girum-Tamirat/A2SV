# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        for i in range(rowIndex+1):
            r = [1] * (i+1)
            for j in range(1, i):
                r[j]=tri[i-1][j-1]+tri[i-1][j]
            tri.append(r)
        return tri[rowIndex]