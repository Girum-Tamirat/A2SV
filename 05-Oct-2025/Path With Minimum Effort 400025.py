# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        min_heap = [(0, 0, 0)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0
        while min_heap:
            curr_effort, r, c = heapq.heappop(min_heap)
            if r == rows - 1 and c == cols - 1:
                return curr_effort
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_effort = max(curr_effort, abs(heights[nr][nc] - heights[r][c]))
                    if next_effort < effort[nr][nc]:
                        effort[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))
        return 0