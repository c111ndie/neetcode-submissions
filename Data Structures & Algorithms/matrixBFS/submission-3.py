class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))
        l = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return l
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            l += 1
        return -1

                
        