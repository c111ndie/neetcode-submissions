class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1

        found = False
        for i, row in enumerate(matrix):
            if row[0] <= target <= row[r]:
                R = i
                found = True
        if not found:
            return False
                
        while l <= r:
            m = (l + r) // 2
            
            if matrix[R][m] < target:
                l = m + 1
            elif matrix[R][m] > target:
                r = m - 1
            elif matrix[R][m] == target:
                return True
        return False
        