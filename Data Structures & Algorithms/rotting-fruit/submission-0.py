class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = collections.deque()
        fresh = 0
        time = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append([i,j]) 
        while fresh > 0 and q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                for i , j in directions:
                    row , col = r + i, c + j
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) 
                    or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -=1
            time +=1
        return time if fresh == 0 else -1            


        