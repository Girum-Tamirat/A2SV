# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur, op, cl):
            if len(cur) == 2*n:
                res.append(cur)
            if op < n:
                backtrack(cur+'(', op+1, cl)
            if cl < op:
                backtrack(cur+')', op, cl+1)
        backtrack("", 0, 0)
        return res
