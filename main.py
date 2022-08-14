import pygame

from models.scene import Scene

from statics.colours import Colours

# config
cell_size = 10
fps = 10

# colours

# session variables
start = False
win = None
# n_cols = s_width // cell_size
# n_rows = s_height // cell_size
rule = []

# global objects
# 2D matrix of cells
# current_grid = []
# new_grid = []

def activate_cell(pix_x, pix_y, env):
    # find the nearest cell on the grid

    # TODO: optimization
    for row in env:
        for cell in row:
            if cell.collidepoint(pix_x, pix_y):
                cell.state = 1
                pygame.draw.rect(win, Colours.green_clr, cell)

                break

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
                pygame.draw.rect(win, Colours.green_clr, cell)
            else:
                pygame.draw.rect(win, Colours.white_clr, cell)
    current_grid = new_grid


def test():
    pass


def init(scene: Scene):
    # global win
    s_width, s_height = 1200, 1200

    # win = pygame.display.set_mode((s_width, s_height))
    # pygame.display.set_caption('Cellular Automata')
    # global clock
    # clock = pygame.time.Clock()

    # create cells based on initial state

    # win.fill(Colours.white_clr)

    global current_grid
    global new_grid
    # current_grid = draw_grid()
    # new_grid = draw_grid()
    scene = Scene(s_width, s_height)
    return scene



def run(scene: Scene):

    global start
    global current_grid
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
                if event.key == pygame.K_SPACE:
                    start = True
                    update_grid()

                if event.key == pygame.K_BACKSPACE:
                    # clear the screen and grid
                    current_grid = scene.grid.draw_grid()
                    start = False
                    pass

            if pygame.mouse.get_focused():
                # if mouse is held down
                # activate the cell under the mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                left, _, _ = pygame.mouse.get_pressed()
                if left:
                    activate_cell(mouse_x, mouse_y, current_grid)

        # compute new grid based on current grid
        if start:
            update_grid()

        pygame.display.update()

        scene.clock.tick(fps)


if __name__ == '__main__':

    # init()

    s_width, s_height = 1200, 1200
    scene = Scene(s_width, s_height)
    scene.grid.draw_grid()
    run(scene=scene)

