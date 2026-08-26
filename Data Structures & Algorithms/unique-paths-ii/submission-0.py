class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * col
        for i in range(row - 1, -1, -1):
            cur = [0] * col
            if obstacleGrid[i][col - 1] != 1:
                if not(i < row - 1 and prev[col - 1] == 0):
                    cur[col - 1] = 1
            for j in range(col - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    cur[j] = prev[j] + cur[j + 1]
                else:
                    cur[j] = 0
            prev = cur  
        return prev[0]