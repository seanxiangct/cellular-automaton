import pygame
import random

# config
s_width, s_height = 600, 600
cell_size = 5

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


class Cell:

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state


def draw_cell(cell):
    if cell.state:
        x_cor = cell.x - cell_size // 2
        y_cor = cell.y - cell_size // 2
        pygame.draw.rect(win, white_clr, (x_cor, y_cor, cell_size, cell_size))


def draw_row():
    row = []


def draw_grid():
    pass


def init():
    global win
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Cellular Automata')
    clock = pygame.time.Clock()

    # create cells based on initial state

    win.fill(black_clr)


def run():

    while run:

        # if key is held down
        keys = pygame.key.get_pressed()

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
                    draw_cell(Cell(mouse_x, mouse_y, 1))

        pygame.display.update()


if __name__ == '__main__':

    init()

    run()

