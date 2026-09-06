class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            row_cnt = [0] * 9
            for j in range(9):
                if board[i][j] != ".":
                    row_cnt[int(board[i][j]) - 1] += 1
                    if row_cnt[int(board[i][j]) - 1] > 1:
                        return False
        for i in range(9):
            col_cnt = [0] * 9
            for j in range(9):
                if board[j][i] != ".":
                    col_cnt[int(board[j][i]) - 1] += 1
                    if col_cnt[int(board[j][i]) - 1] > 1:
                        return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                box_cnt = [0] * 9
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] != ".":
                            box_cnt[int(board[r][c]) - 1] += 1
                            if box_cnt[int(board[r][c]) - 1] > 1:
                                return False
        return True

