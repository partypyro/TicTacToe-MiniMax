import pygame


def multiply_tuples(a, b):
    return tuple((x * y) for x, y in zip(a, b))

def add_tuples(a, b):
    return tuple((x + y) for x, y in zip(a, b))

class Renderer:
    xImg = pygame.image.load('X.png')
    oImg = pygame.image.load('O.png')
    BOARD_WIDTH = 3
    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self, display, board_pos, board_size):
        self.display = display
        self.board_pos = board_pos
        self.board_size = board_size
        self.display_size = display.get_size()
        self.image_scale = (self.board_size[0] // self.BOARD_WIDTH, self.board_size[1] // self.BOARD_WIDTH)
        self.xImg = pygame.transform.smoothscale(self.xImg, self.image_scale)
        self.oImg = pygame.transform.smoothscale(self.oImg, self.image_scale)

    def draw_x(self, x, y):
        coords = add_tuples(self.board_pos, multiply_tuples(self.image_scale, (x, y)))
        self.display.blit(self.xImg, coords)

    def draw_o(self, x, y):
        coords = add_tuples(self.board_pos, multiply_tuples(self.image_scale, (x, y)))
        self.display.blit(self.oImg, coords)

    def draw_grid(self):
        # First vertical line
        start_pos =  (self.board_pos[0] + self.image_scale[0], self.board_pos[1])
        end_pos = (self.board_pos[0] + self.image_scale[0], self.board_pos[1] + self.board_size[1])
        pygame.draw.line(self.display, self.black, start_pos, end_pos, 8)

        # Second vertical line
        start_pos = (self.board_pos[0] + (2 * self.image_scale[0]), self.board_pos[1])
        end_pos = (self.board_pos[0] + (2 * self.image_scale[0]), self.board_pos[1] + self.board_size[1])
        pygame.draw.line(self.display, self.black, start_pos, end_pos, 8)

        # First horizontal line
        start_pos = (self.board_pos[0], self.board_pos[1] + self.image_scale[1])
        end_pos = (self.board_pos[0] + self.board_size[0], self.board_pos[1] + self.image_scale[1])
        pygame.draw.line(self.display, self.black, start_pos, end_pos, 8)

        # Second horizontal line
        start_pos = (self.board_pos[0], self.board_pos[1] + (2 * self.image_scale[1]))
        end_pos = (self.board_pos[0] + self.board_size[0], self.board_pos[1] + (2 * self.image_scale[1]))
        pygame.draw.line(self.display, self.black, start_pos, end_pos, 8)

    def draw_marks(self, board):
        # Iterate through the board array and draw the marks
        board_array = board.board_array
        for i, x in enumerate(board_array):
            for j, y in enumerate(x):
                if y == 1:
                    self.draw_x(i, j)
                if y == 0:
                    self.draw_o(i, j)

    #
    def draw_crossthru(self, start_pos, end_pos):
        start_px = multiply_tuples(start_pos, self.image_scale)
        start_px = add_tuples(start_px, multiply_tuples(self.image_scale, (0.5, 0.5)))
        start_px = add_tuples(start_px, self.board_pos)
        end_px = multiply_tuples(end_pos, self.image_scale)
        end_px = add_tuples(end_px, multiply_tuples(self.image_scale, (0.5, 0.5)))
        end_px = add_tuples(end_px, self.board_pos)

        pygame.draw.line(self.display, self.white, start_px, end_px, 16)
        pygame.draw.line(self.display, self.black, start_px, end_px, 8)

    def get_clicked_pos(self, window_pos):
        pos = tuple((a - b) for a, b in zip(window_pos, self.board_pos))
        pos = tuple((a / b) for a, b in zip(pos, self.image_scale))
        pos = tuple(int(a) for a in pos)
        for i in pos:
            if i > self.BOARD_WIDTH - 1 or i < 0:
                return -1, -1
        return pos
