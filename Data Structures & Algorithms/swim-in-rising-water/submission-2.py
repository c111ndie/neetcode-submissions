class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(minHeap, [new_time, nr, nc])

        