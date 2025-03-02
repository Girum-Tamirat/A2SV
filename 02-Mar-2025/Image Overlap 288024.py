# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        mo = 0
        
        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                o = 0
                for i in range(n):
                    for j in range(n):
                        if 0 <= i + dy < n and 0 <= j + dx < n:
                            if img1[i][j] == 1 and img2[i + dy][j + dx] == 1:
                                o += 1
                mo = max(mo, o)
        
        return mo