# Title: Tic-Tac-Toe MiniMax
#
# Author: Aiden Neill
#
# Purpose: This program has a two-fold purpose ->
#   1. To provide a simple, graphical implementation of a
#      Tic-Tac-Toe game in Python using PyGame, with automatic
#      winner detection
#   2. To solve the game of Tic-Tac-Toe with an AI agent
#      that uses a recursive tree search with the minimax
#      algorithm


import pygame

from AIPlayer import AIPlayer
from Render import Renderer
from Board import Board, check_winner

pygame.init()

# Define the size of the game window
display_width = 1000
display_height = 1000

# Define the location of the tic-tac-toe board and how large it will be
board_pos = (0, 0)
board_size = (600, 600)

# Define rgb values for the white and black colors used
black = (0,0,0)
white = (255,255,255)

is_closed = False
is_x_turn = True
is_game_over = False

# Define an integer value correlating to the game winner - O = 0, X = 1, Draw = 2
winner = 2

# Setup winner messages
font = pygame.font.SysFont('ubuntu.tts', 96)
x_wins_text = font.render('X WINS!', True, black)
o_wins_text = font.render('O WINS!', True, black)
draw_text = font.render("IT'S A DRAW!", True, black)

# Open the display, set the title
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic Tac Toe')

# Initiate the clock to set a constant framerate
clock = pygame.time.Clock()

board = Board()
renderer = Renderer(display = gameDisplay, board_pos = board_pos, board_size = board_size)
player_ai = AIPlayer(False)

while not is_closed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_closed = True
        window_pos = (0, 0)
        # If the player clicks on his turn and the game is not over
        if event.type == pygame.MOUSEBUTTONUP and not is_game_over and is_x_turn:
            # Draw the player's mark on the game board where they clicked
            window_pos = pygame.mouse.get_pos()
            board.set_value(renderer.get_clicked_pos(window_pos), is_x_turn)

            # Change the turn to the ai play
            is_x_turn = not is_x_turn

            # Check who won (if there is a winner)
            winner = check_winner(board.board_array)
            # If the game is not a draw and there is a winner, set the game as over
            if winner[0] != 2:
                is_game_over = True
                print(winner[0], " wins")

        # If it is the AI agent's turn, and the game is not over
        if not is_x_turn and not is_game_over:
            # Give the agent the game board to find the winning line of moves
            winning_line = player_ai.best_move(board=board.board_array, is_x_turn=is_x_turn)
            print(winning_line[1])
            # Make the best move, the first move in the winning line of moves
            board.set_value(winning_line[1], is_x_turn)
            # Change the turn back to the player
            is_x_turn = not is_x_turn
            winner = check_winner(board.board_array)
            if winner[0] != 2:
                is_game_over = True
                print(winner[0], " wins")

    # CLear the display
    gameDisplay.fill(white)

    renderer.draw_grid()
    renderer.draw_marks(board)

    # Draw the line through the winning marks and draw the winner text
    if is_game_over:
        if winner[0] == 1:
            renderer.draw_crossthru(winner[1], winner[2])
            gameDisplay.blit(x_wins_text, (board_pos[0] + 100, board_pos[1] + board_size[1] + 100))
        if winner[0] == 0:
            renderer.draw_crossthru(winner[1], winner[2])
            gameDisplay.blit(o_wins_text, (board_pos[0] + 100, board_pos[1] + board_size[1] + 100))
        if winner[0] == 3:
            gameDisplay.blit(draw_text, (board_pos[0] + 100, board_pos[1] + board_size[1] + 100))

    pygame.display.update()
    clock.tick(20)

pygame.quit()
quit()


