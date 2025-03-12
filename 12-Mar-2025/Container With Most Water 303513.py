# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, ma = 0, len(height)-1, 0
        while i < j:
            ch = min(height[i],height[j]) * (j-i)
            ma = max(ch, ma)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ma