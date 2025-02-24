# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0 
        obstacles_set = set(map(tuple, obstacles)) 
        max_distance = 0
        
        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2: 
                d = (d - 1) % 4
            else:
                for _ in range(command):
                    new_x, new_y = x + directions[d][0], y + directions[d][1]
                    if (new_x, new_y) in obstacles_set:
                        break 
                    x, y = new_x, new_y
                    max_distance = max(max_distance, x**2 + y**2)        
        return max_distance