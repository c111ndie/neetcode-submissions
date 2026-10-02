class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            cnt = 0
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            cnt += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                cnt += dfs(nr, nc)
            return cnt
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(dfs(r, c), max_area)
        return max_area
                    
                
        