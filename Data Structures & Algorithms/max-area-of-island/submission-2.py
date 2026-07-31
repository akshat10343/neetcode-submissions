class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        highest = 0
        #visited = set()

        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 1:
                return
            grid[i][j] = 0
            self.temp += 1
            dfs(i +1,j)
            dfs(i,j+1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.temp = 0
                    dfs(i,j)
                    highest = max(self.temp, highest)

        return highest
