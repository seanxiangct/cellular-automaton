import pygame
import random
import utils

# config
s_width, s_height = 800, 800
cell_size = 10
fps = 1

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
states = [0, 1]
occurrence = [0.8, 0.2]

# global objects
# 2D matrix of cells
current_grid = []
new_grid = []
clock = None


class Cell(pygame.Rect):

    def __init__(self, x, y, state=0):
        super(Cell, self).__init__(x, y, cell_size, cell_size)
        self.x = x
        self.y = y
        self.i_x = self.x // cell_size
        self.i_y = self.y // cell_size
        self.state = state

    def get_neighbours(self, grid):
        neighbours = []
        for j in range(self.i_y - 1, self.i_y + 2):
            for i in range(self.i_x - 1, self.i_x + 2):
                try:
                    neighbours.append(grid[i][j])
                except IndexError:
                    break
        return neighbours

    def update(self, env):
        if self.state == 1 and (env < 2 or env > 3):
            self.state = 0
        elif self.state == 0 and env == 3:
            self.state = 1
        return self.state


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def activate_cell(pix_x, pix_y, env):
    # find the nearest cell on the grid

    # TODO: optimization
    for row in env:
        for cell in row:
            if cell.collidepoint(pix_x, pix_y):
                cell.state = 1
                pygame.draw.rect(win, black_clr, cell)

                break


def draw_grid():

    grid = []
    x_cor = 0
    y_cor = 0
    for j in range(n_cols):
        row = []
        for i in range(n_rows):
            cell = Cell(x_cor + j * cell_size, y_cor + i * cell_size, random.choices(states, occurrence)[0])
            row.append(cell)
            pygame.draw.rect(win, black_clr, cell, 1)
        grid.append(row)
    return grid


def test():
    pass


def init():
    global win
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Cellular Automata')
    global clock
    clock = pygame.time.Clock()

    # create cells based on initial state

    win.fill(white_clr)

    global current_grid
    global new_grid
    current_grid = draw_grid()
    new_grid = draw_grid()


def update_grid():
    global current_grid
    for row in current_grid:
        for cell in row:
            neighbours = cell.get_neighbours(current_grid)
            life_count = 0
            for n in neighbours:
                if n.state == 1:
                    life_count += 1
            new_state = cell.update(life_count)
            new_grid[cell.i_x][cell.i_y].state = new_state
            if new_state:
                pygame.draw.rect(win, red_clr, cell)
            else:
                pygame.draw.rect(win, white_clr, cell)
    current_grid = new_grid


def run():

    while run:

        # print(clock.get_fps())
        # handles input
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
                left, right, middle = pygame.mouse.get_pressed()
                if left:
                    activate_cell(mouse_x, mouse_y, current_grid)

        # compute new grid based on current grid
        update_grid()

        pygame.display.update()

        clock.tick(fps)


if __name__ == '__main__':

    init()

    run()

