from collections import defaultdict


class Solution:
    def solveSudoku(self, board):
        """约束编程与回溯backtrace
        回溯函数如下：
        backtrack(row = 0, col = 0)。
        从最左上角的方格开始 row = 0, col = 0。直到到达一个空方格。
        从1 到 9 迭代循环数组，尝试放置数字 d 进入 (row, col) 的格子。
        如果数字 d 还没有出现在当前行，列和子方块中：
        将 d 放入 (row, col) 格子中。
        记录下 d 已经出现在当前行，列和子方块中。
        如果这是最后一个格子row == 8, col == 8 ：
        意味着已经找出了数独的解。
        否则
        放置接下来的数字。
        如果数独的解还没找到：
        将最后的数从 (row, col) 移除。
        """

        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1  # defaultdict类，rows[row][d]是数字d在rows[row]中出现的次数。
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved  # nonlocal声明用来修改嵌套作用域的变量
                sudoku_solved = True
            # if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            1.从选项列表中作出选择
            2.执行回溯函数backtrace()
            3.若当前选择无法实现既定目标，则删除当前选择。
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index：0~(N-1)
        box_index = lambda row, col: (row // n) * n + col // n

        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]  # rows中存储的defaultdict类
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()


if __name__ == '__main__':
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.solveSudoku(board))
