# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        c = 0
        ans = []
        cs = []
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            q = Counter(mat[i])
            c = q.get(1, 0)
            cs.append(c)
        ind = cs.index(max(cs))
        ans.append(ind)
        ans.append(max(cs))
        return ans
            
            
