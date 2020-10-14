def check_winner(board):
    num_of_moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 2:
                num_of_moves += 1
    if num_of_moves == 9: return 3, (0, 0), (0, 0)

    for i in range(3):
        num_x = 0
        num_o = 0
        for j in range(3):
            if board[i][j] == 1:
                num_x += 1
            if board[i][j] == 0:
                num_o += 1
        if num_x == 3: return 1, (i, 0), (i, j)
        if num_o == 3: return 0, (i, 0), (i, j)

    for j in range(3):
        num_x = 0
        num_o = 0
        for i in range(3):
            if board[i][j] == 1:
                num_x += 1
            if board[i][j] == 0:
                num_o += 1
        if num_x == 3: return 1, (0, j), (i, j)
        if num_o == 3: return 0, (0, j), (i, j)

    num_x = 0
    num_o = 0
    for i in range(3):
        if board[i][i] == 1:
            num_x += 1
        if board[i][i] == 0:
            num_o += 1
    if num_x == 3: return 1, (0, 0), (2, 2)
    if num_o == 3: return 0, (0, 0), (2, 2)

    num_x = 0
    num_o = 0
    for i in range(3):
        if board[i][2-i] == 1:
            num_x += 1
        if board[i][2-i] == 0:
            num_o += 1
    if num_x == 3: return 1, (0, 2), (2, 0)
    if num_o == 3: return 0, (0, 2), (2, 0)
    return 2, (0, 0), (0, 0)


class Board:
    board_array = [[2, 2, 2],
                  [2, 2, 2],
                  [2, 2, 2]]

    def __init__(self, board = None):
        if board is not None: self.board_array = board

    def set_value(self, pos, value):
        for i in pos:
            if i < 0:
                return
        if self.board_array[pos[0]][pos[1]] == 2:
            self.board_array[pos[0]][pos[1]] = value

    def clear_board(self):
        self.board_array = [[2, 2, 2],
                      [2, 2, 2],
                      [2, 2, 2]]

