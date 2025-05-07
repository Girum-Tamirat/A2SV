# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = [elem for row in matrix for elem in row]
        mat.sort()
        l, r = 0, len(mat)-1
        while l <= r:
            m = (l+r)//2
            if target>mat[m]:
                l=m+1
            elif target<mat[m]:
                r=m-1
            else:
                return True
        return False