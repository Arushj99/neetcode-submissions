class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''Create a list for the directions that you can move in, and then
        iterate through the matrix to locate the first 1. Then look at it's adjacent
        elements by applying direction to the current row/col, and if the new position 
        is 1, then convert it to 0, but if it is already 0, then just return'''
        direction = [[-1,0], [1, 0], [0, 1], [0, -1]]
        row = len(grid)
        col = len(grid[0])
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return 

            for dr, dc in direction:
                dfs(r + dc, c + dr)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1

        return islands
                
        