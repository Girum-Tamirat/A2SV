# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = defaultdict(list)
        rows, cols  = len(mat), len(mat[0])
        
        for i in range(rows):
            for j in range(cols):
                diags[i + j].append(mat[i][j])
        ans = []
        for key in range(rows + cols - 1):
            if key % 2 == 0:
                ans.extend(reversed(diags[key]))
            else:
                ans.extend(diags[key])
        return ans
        