class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        first_row = 1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = 0
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(col):
                    matrix[i][j] = 0
        for i in range(col):
            if matrix[0][i] == 0:
                for j in range(row):
                    matrix[j][i] = 0   
        if first_row == 0:
            for j in range(col):
                matrix[0][j] = 0     
            
        
        