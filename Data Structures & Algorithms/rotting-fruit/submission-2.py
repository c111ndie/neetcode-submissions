class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if min((r + dr), (c + dc)) < 0 or r + dr == rows or c + dc == cols or grid[r + dr][c + dc] !=  1:
                        continue
                    grid[r + dr][c + dc] = 2
                    fresh -= 1
                    q.append((r + dr, c + dc))
            minutes += 1
        if fresh > 0:
            return -1
        return minutes
            
        