# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stc, cur = [], 0
        for i in s:
            if i == '(':
                stc.append(cur)
                cur = 0
            else:
                cur += stc.pop() + max(cur, 1)
        return cur