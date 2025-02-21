# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

        # tr = [[None]*len(matrix) for _ in range(len(matrix[0]))]
        # for i, row in enumerate(matrix):
        #     for j, val in enumerate(row):
        #         tr[j][i] = val
        # return tr
