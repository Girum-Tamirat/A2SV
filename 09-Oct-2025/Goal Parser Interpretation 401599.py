# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        a = []
        i = len(command)-1
        while i>=0:
            if command[i] == ')':
                if command[i-1] == 'l':
                    a.append("al")
                    i-=4
                else:
                    a.append("o")
                    i-=2
            else:
                a.append("G")
                i-=1
        return ''.join(reversed(a))