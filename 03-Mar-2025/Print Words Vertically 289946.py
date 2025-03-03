# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        rows = s.split(" ") 
        max_len = max(len(word) for word in rows)
        
        tr = ["".join(rows[i][j] if j < len(rows[i]) else " " for i in range(len(rows))) for j in range(max_len)]
        
        return [t.rstrip() for t in tr]