# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for x, y in redEdges:
            g1[x].append(y)
        for x, y in blueEdges:
            g2[x].append(y)
            
        q = deque()
        q.append((0, 0, 0))
        q.append((0, 1, 0))
        
        v = [[False] * 2 for _ in range(n)]
        v[0][0] = True
        v[0][1] = True
        
        ans = [-1] * n
        ans[0] = 0
        
        while q:
            a, b, c = q.popleft()
            if b == 0:
                nxt = g2[a]
                col = 1
            else:
                nxt = g1[a]
                col = 0
            for d in nxt:
                if not v[d][col]:
                    v[d][col] = True
                    q.append((d, col, c + 1))
                    if ans[d] == -1:
                        ans[d] = c + 1
        return ans