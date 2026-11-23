class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < row and 0 <= nc < col) or (nr, nc) in visited or grid[nr][nc] == -1:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                    