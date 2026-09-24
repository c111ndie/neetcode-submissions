class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        length = 0
        visit = set()
        while q:
            length += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or grid[r + dr][c + dc] == -1 or (r + dr, c + dc) in visit:
                        continue
                    if grid[r + dr][c + dc] == INF:
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = length

