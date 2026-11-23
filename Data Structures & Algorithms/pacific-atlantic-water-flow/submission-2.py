class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac = set()
        atl = set()
        row, col = len(heights), len(heights[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def dfs(r, c, visit, ocean):
            if ocean == "pac":
                pac.add((r, c))
            elif ocean == "atl":
                atl.add((r, c))
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < row and 0 <= nc < col) or (nr, nc) in visit or heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visit, ocean)
            return
        for r in range(row):
            for c in range(col):
                if r == 0:
                    dfs(r, c, set(), "pac")
                if c == 0 and r > 0:
                    dfs(r, c, set(), "pac")
                if r == row - 1:
                    dfs(r, c, set(), "atl")
                if c == col - 1 and r < row - 1:
                    dfs(r, c, set(), "atl")
        for r in range(row):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res