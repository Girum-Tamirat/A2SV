# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        result = [[None]*rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                result[i][j] = image[i][cols-1-j] ^ 1
        return result
