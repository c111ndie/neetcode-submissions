class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        u, d = 0, row - 1
        target_r = -1
        while u <= d:
            m = (u + d) // 2
            if (m < d and matrix[m][0] <= target < matrix[m+1][0]) or m == d:
                target_r = m
                break
            elif matrix[m][0] < target:
                u = m + 1
            elif matrix[m][0] > target:
                d = m - 1
        if target_r == -1:
            return False
        l, r = 0, col - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[target_r][m] < target:
                l = m + 1
            elif matrix[target_r][m] > target:
                r = m - 1
            else:
                return True
        return False