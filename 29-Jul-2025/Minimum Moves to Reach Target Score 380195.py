# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, t: int, m: int) -> int:
        c = 0
        while t>1 and m>0:
            if t%2==0:
                t//=2
                m-=1
            else:
                t-=1
            c+=1
        if t>1:
            c += t-1
        return c