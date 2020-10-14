import copy

from Board import check_winner


class AIPlayer:
    def __init__(self, is_x_player):
        self.is_x_player = is_x_player

    def get_possible_moves(self, board):
        possible_moves = list()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 2:
                    possible_moves.append((i, j))
        return possible_moves

    def best_line(self, board, is_x_turn):
        possible_moves = self.get_possible_moves(board)
        winner = check_winner(board)
        if winner[0] != 2:
            if winner[0] == 1:
                return 1
            elif winner[0] == 0:
                return -1
            elif winner[0] == 3:
                return 0
        else:
            possible_move_evaluations = list()
            for move in possible_moves:
                branch = copy.deepcopy(board)
                branch[move[0]][move[1]] = is_x_turn
                move_eval = self.best_line(branch, not is_x_turn)
                possible_move_evaluations.append(move_eval)
            if is_x_turn:
                # Maximize
                evaluation = max(possible_move_evaluations)
            else:
                # Minimize
                evaluation = min(possible_move_evaluations)
            return evaluation

    def best_move(self, board, is_x_turn):
        possible_moves = self.get_possible_moves(board)
        possible_move_evaluations = list()
        evaluation_list = list()
        for move in possible_moves:
            branch = copy.deepcopy(board)
            branch[move[0]][move[1]] = is_x_turn
            move_eval = self.best_line(branch, not is_x_turn)
            evaluation_list.append(move_eval)
            possible_move_evaluations.append([move_eval, move])
        evaluation = 0
        if is_x_turn:
            # Maximize
            evaluation = max(evaluation_list)
        else:
            # Minimize
            evaluation = min(evaluation_list)
        return possible_move_evaluations[evaluation_list.index(evaluation)]

