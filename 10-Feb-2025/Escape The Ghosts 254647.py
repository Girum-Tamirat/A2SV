# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mydis = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghodis = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghodis <= mydis:
                return False
        return True
