class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cells = []
        dp = [[1] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                cells.append((matrix[r][c], r, c))
        cells.sort(reverse = True)
        answer = 1 
        for cell, r, c in cells:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])
            answer = max(answer, dp[r][c])
        return answer