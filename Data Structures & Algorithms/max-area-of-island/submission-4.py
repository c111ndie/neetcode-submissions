class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visit = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] != 1 or (r, c) in visit:
                return 0
            area = 1
            visit.add((r, c))
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))
        return max_area

            