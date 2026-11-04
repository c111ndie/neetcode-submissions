class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            nums = set()
            for c in range(9):
                if board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != ".":
                    return False
        for c in range(9):
            nums = set()
            for r in range(9):
                if board[r][c] not in nums:
                    nums.add(board[r][c])
                elif board[r][c] != ".":
                    return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] not in nums:
                            nums.add(board[r+i][c+j])
                        elif board[r+i][c+j] != ".":
                            return False
        return True