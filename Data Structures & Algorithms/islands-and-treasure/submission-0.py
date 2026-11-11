class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        INF = 2147483647

        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i,j])
        while q:
            r , c = q.popleft()
            for nr,nc in directions:
                row, col = r+nr,c+nc
                if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == INF):
                    grid[row][col] = grid[r][c]+1
                    q.append([row,col])


   


