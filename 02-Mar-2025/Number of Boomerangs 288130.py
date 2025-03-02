# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
    
        for i in range(len(points)):
            dm = {}
            
            for j in range(len(points)):
                if i == j:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                distance = dx**2 + dy**2
                
                if distance not in dm:
                    dm[distance] = 0
                dm[distance] += 1
            
            for count in dm.values():
                if count > 1:
                    result += count * (count - 1)
                    
        return result