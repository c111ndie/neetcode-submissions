class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if (min(r, c) < 0 or r > rows - 1 or c > cols - 1 or 
            grid[r][c] == 0):
                return 0
            area = 1
            grid[r][c] = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area

            
        