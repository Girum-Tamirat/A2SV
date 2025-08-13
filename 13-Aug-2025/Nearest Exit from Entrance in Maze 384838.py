# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        v = [[False]*n for _ in range(m)]
        v[entrance[0]][entrance[1]] = True
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x, y, s = q.popleft()
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and not v[nx][ny]:
                    if nx in (0, m-1) or ny in (0, n-1):
                        return s+1
                    v[nx][ny] = True
                    q.append((nx, ny, s+1))
        return -1