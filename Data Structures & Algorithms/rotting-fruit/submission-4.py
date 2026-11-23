class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        row, col = len(grid), len(grid[0])
        q = deque()
        t = 0
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1) or (nr, nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    grid[r][c] = 2
                    fresh -= 1
            t += 1
        if fresh == 0:
            return t
        else:
            return -1
