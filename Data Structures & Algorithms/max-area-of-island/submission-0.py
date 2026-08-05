class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        area = 0
        def dfs(r, c):
            nonlocal max_area, area
            if (min(r, c) < 0 or r > rows - 1 or c > cols - 1 or 
            grid[r][c] == 0):
                return
            area += 1
            grid[r][c] = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            if area > max_area:
                max_area = area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
        return max_area

            
        