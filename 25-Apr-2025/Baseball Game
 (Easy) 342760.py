# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stc = []
        for op in ops:
            if op.lstrip('-').isdigit():
                stc.append(int(op))
            elif op == "+":
                stc.append(stc[-1] + stc[-2])
            elif op == "D":
                stc.append(2*stc[-1])
            elif op == "C":
                stc.pop()
            print(stc)
        return sum(stc)