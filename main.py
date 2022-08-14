import logging
import pygame

from models.scene import Scene

# config
cell_size = 10
fps = 10

# colours

# session variables
# n_cols = s_width // cell_size
# n_rows = s_height // cell_size
rule = []
def run(scene: Scene):

    start = False
    while run:

        # print(clock.get_fps())
        # handles input
        # if key is held down
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # if key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    logging.info('Quitting')
                    # exit
                    return
                if event.key == pygame.K_SPACE:
                    start = True
                    if not scene.grid:
                        scene.grid.draw_grid()

                if event.key == pygame.K_BACKSPACE:
                    # clear the screen and grid
                    # current_grid = scene.grid
                    scene.grid.draw_grid()
                    start = False
                    logging.info('Reset world')
                    continue
                    
                if event.key == pygame.K_m:
                    logging.info('Manual mode')
                    start = False
                    scene.set_mode(gen_grid=False)
                    scene.grid.draw_grid()
                    continue
                
                if event.key == pygame.K_o:
                    logging.info('Automatic mode')
                    start = True
                    scene.set_mode(gen_grid=True)
                    scene.grid.draw_grid()
                    continue

            if pygame.mouse.get_focused():
                # if mouse is held down
                # activate the cell under the mouse
                mouse_x, mouse_y = pygame.mouse.get_pos()
                left, _, _ = pygame.mouse.get_pressed()
                if left:
                    scene.grid.activate_cell(mouse_x, mouse_y)

        # compute new grid based on current grid
        if start:
            logging.info('Starting')
            scene.grid.update_grid()
        else:
            logging.info('Paused')

        pygame.display.update()

        scene.clock.tick(fps)


if __name__ == '__main__':

    # init()
    logger_format = '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'
    logger_datefmt = '%d/%b/%Y %H:%M:%S'
    logging.basicConfig(
        level=logging.DEBUG,
        format=logger_format,
        datefmt=logger_datefmt)

    s_width, s_height = 1200, 1200
    scene = Scene(s_width, s_height)
    run(scene=scene)

