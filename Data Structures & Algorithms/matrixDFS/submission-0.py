class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        def count(grid, r, c, visited):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 1:
                return 0
            elif r == ROWS - 1 and c == COLS - 1:
                return 1
            visited.add((r, c))
            cnt = 0
            cnt += count(grid, r - 1, c, visited)
            cnt += count(grid, r, c - 1, visited)
            cnt += count(grid, r + 1, c, visited)
            cnt += count(grid, r, c + 1, visited)
            visited.remove((r, c))
            return cnt
        return count(grid, 0, 0, visited)