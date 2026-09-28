class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        memo = {}
        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            longest = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))
            memo[(r, c)] = longest
            return memo[(r, c)]
        maxLen = 0
        for r in range(rows):
            for c in range(cols):
                maxLen = max(maxLen, dfs(r, c))
        return maxLen

        