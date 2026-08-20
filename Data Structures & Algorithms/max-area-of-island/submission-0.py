class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ''' Do the same method as I did for number of islands, but 
        this time have a global variable that also keeps count of the max between 
        the number of times a 1 is seen in dfs and the current max'''

        direction = [(-1,0), (1,0), (0,1), (0,-1)]
        row = len(grid)
        col = len(grid[0])
        maxIslands = 0

        def dfs(r, c):
            numIslands = 0
            if r < 0 or c < 0 or r >= row or c >= col:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if grid[r][c] == 1:
                grid[r][c] = 0
                numIslands += 1
            for dr, dc in direction:
                numIslands += dfs(r+dr, c+dc)
            
            return numIslands

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    maxIslands = max(maxIslands, dfs(r,c))
        return maxIslands