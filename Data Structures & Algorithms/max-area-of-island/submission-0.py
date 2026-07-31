class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        highest = []
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
                    highest.append(self.temp)
        highest = sorted(highest)
        if len(highest) == 0:
            return 0
        return highest[-1]

