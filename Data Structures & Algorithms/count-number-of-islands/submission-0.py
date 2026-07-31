class Solution:
     def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])

        def dfs(row, cols):
            if row < 0 or row >= r or cols < 0 or cols >= c or grid[row][cols] != "1":
                return
            else:
                grid[row][cols] = "0"
                dfs(row + 1, cols)
                dfs(row, cols + 1)
                dfs(row - 1, cols)
                dfs(row, cols - 1)




        island = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i,j)
        return island
