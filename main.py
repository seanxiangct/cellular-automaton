import pygame
import random
import utils

# config
s_width, s_height = 800, 800
cell_size = 10

# colours
red_clr = (255, 0, 0)
green_clr = (0, 255, 0)
blue_clr = (0, 0, 255)
black_clr = (0, 0, 0)
white_clr = (255, 255, 255)

# session variables
win = None
n_cols = s_width // cell_size
n_rows = s_height // cell_size
rule = []
initial_state = [random.randint(0, 1) for x in range(n_cols)]

# 2D matrix of cells
grid = []


class Cell(pygame.Rect):

    def __init__(self, x, y, state=1):
        super(Cell, self).__init__(x, y, cell_size, cell_size)
        self.x = x
        self.y = y
        self.state = state


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def activate_cell(pix_x, pix_y):
    # find the nearest cell on the grid
    # pygame.draw.rect(win, black_clr, (x_cor, y_cor, cell_size, cell_size))
    in_rect = utils.binary_search_2d(Point(pix_x, pix_y), grid)
    pygame.draw.rect(win, black_clr, in_rect)


def draw_grid():

    x_cor = 0
    y_cor = 0
    for j in range(n_cols):
        row = []
        for i in range(n_rows):
            cell = Cell(x_cor + j * cell_size, y_cor + i * cell_size)
            row.append(cell)
            pygame.draw.rect(win, black_clr, cell, 1)
        grid.append(row)


def test():
    pass


def init():
    global win
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Cellular Automata')
    clock = pygame.time.Clock()

    # create cells based on initial state

    win.fill(white_clr)

    draw_grid()


def run():

    while run:

        # if key is held down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            test()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # if key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # exit
                    return

            if pygame.mouse.get_focused():
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if keys[pygame.K_SPACE]:
                    # pygame.draw.circle(win, red_clr, (mouse_x, mouse_y), 3)
                    activate_cell(mouse_x, mouse_y)

        pygame.display.update()


if __name__ == '__main__':

    init()

    run()

