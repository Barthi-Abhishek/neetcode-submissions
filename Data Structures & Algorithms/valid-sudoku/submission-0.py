class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(0,9)]
        column = [set() for _ in range(0,9)]
        boxes = [set() for _ in range(0,9)]

        for r in range(0,9):
            for c in range(0,9):
                if board[r][c] == ".":
                    continue
                box_index = (r//3)*3 + (c//3)

                # putting row values in row list containing indexed sets
                if board[r][c] in rows[r]:
                    return False
                # putting column values in row list containing indexed sets
                elif board[r][c] in column[c]:
                    return False
                # putting 3x3 grid  values in row list containing indexed sets
                elif board[r][c] in boxes[box_index]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    column[c].add(board[r][c])
                    boxes[box_index].add(board[r][c])

        return True

                

       



        

        