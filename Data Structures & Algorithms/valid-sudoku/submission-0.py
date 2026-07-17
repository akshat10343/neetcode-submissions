class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board[0])):
            check = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    if board[i][j] in check:
                        return False
                    else:
                        check.add(board[i][j])
            check = set()
            for j in range(len((board[0]))):
                if board[j][i].isdigit():
                    if board[j][i] in check:
                        return False
                    else:
                        check.add((board[j][i]))

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                check = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[i+row_start][j+col_start].isdigit():
                            if board[i+row_start][j+col_start] in check:
                                return False
                            else:
                                check.add(board[i+row_start][j+col_start])
        return True