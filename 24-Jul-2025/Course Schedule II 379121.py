# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg  = [0]*n
        for v, u in prerequisites:
            graph[u].append(v)
            indeg[v] += 1
        q = deque([i for i in range(n) if indeg[i] == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return order if len(order) == n else []