class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cnt = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    dfs(nr, nc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c)
                else:
                    continue
        return cnt
        