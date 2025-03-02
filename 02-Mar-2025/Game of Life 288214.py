# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        def count_live_neighbors(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                    count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2  

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0 
                elif board[i][j] == 2:
                    board[i][j] = 1