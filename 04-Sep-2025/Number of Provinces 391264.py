# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        prov = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                prov += 1
        return prov