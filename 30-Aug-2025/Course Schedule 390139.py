# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indeg[course] += 1
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return visited == numCourses