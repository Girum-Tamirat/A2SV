# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mn = blocks[:k].count("W")
        x = mn
        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                x -= 1
            if blocks[i] == "W":
                x += 1
            mn = min(mn, x)
        return mn