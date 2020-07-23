class Solution:
    def isValidSudoku(self, board):
        # initiate data
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        # valid box
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_index = (i // 3) * 3 + (j // 3)
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1  # assign occurrences of num to keys把key值(num)出现次数赋值给键num
                    columns[i][num] = columns[i].get(num, 0) + 1
                    boxes[i][num] = boxes[i].get(num, 0) + 1
                    # check whether the value has already been stored before
                    if boxes[i][num] > 1 or columns[i][num] > 1 or rows[i][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.isValidSudoku(board))
