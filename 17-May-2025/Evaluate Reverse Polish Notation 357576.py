# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stc = []
        for tok in tokens:
            if len(tok) > 1 or tok.isdigit():
                stc.append(int(tok))
            else:
                b = stc.pop()
                a = stc.pop()
                if tok == "+":
                    stc.append(a + b)
                elif tok == "-":
                    stc.append(a - b)
                elif tok == "*":
                    stc.append(a * b)
                else:
                    stc.append(int(a / b))
        return stc[0]