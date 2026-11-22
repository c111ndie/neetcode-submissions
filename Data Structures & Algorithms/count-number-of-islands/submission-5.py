class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        row, col = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col and grid[r][c] == "1"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res