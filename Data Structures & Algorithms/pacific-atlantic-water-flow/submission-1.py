class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, ocean):
            if (
                r < 0 or r == rows
                or c < 0 or c == cols
                or (r, c) in ocean):
                return
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in ocean:
                ocean.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                if 0 <= r + dr < rows and 0 <= c + dc < cols and heights[r + dr][c + dc] >= heights[r][c]:
                    dfs(r + dr, c + dc, ocean)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if (r, c) in pacific and (r, c) in atlantic
        ]