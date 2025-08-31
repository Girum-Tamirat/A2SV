# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  
        for start in range(n):
            if color[start] != 0:  
                continue
            queue = deque([start])
            color[start] = 1  
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0: 
                        color[neighbor] = -color[node] 
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]: 
                        return False
        return True