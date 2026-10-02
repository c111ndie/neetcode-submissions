class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time = 0
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft() 
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue
                    else:
                        grid[r + dr][c + dc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1  
        if fresh > 0:
            return -1
        else:
            return time
        