# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n
        def solve(i):
            if i>= n: return 0
            if dp[i]!=-1: return dp[i]
            p, s = questions[i]
            t = p + solve(i + s + 1)
            x = solve(i + 1)
            dp[i] = max(t, x)
            return dp[i]
        return solve(0)