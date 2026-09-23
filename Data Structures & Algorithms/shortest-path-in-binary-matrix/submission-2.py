class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque([(0, 0)])
        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                visit.add((r, c))
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1
                    

        