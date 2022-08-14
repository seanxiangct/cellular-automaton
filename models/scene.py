import pygame

from models.grid import Grid
from statics.colours import Colours

class Scene:

    cell_size = 10
    death_rate = 0.05
    gen_grid = True

    def __init__(self, width, height) -> None:
        self.scene = pygame.display.set_mode((width, height))
        # self.scene.set_caption('Cellular Automata')
        pygame.display.set_caption('Cellular Automata')
        self.scene.fill(Colours.white_clr)

        self.clock = pygame.time.Clock()

        self.grid = Grid(self.scene, width, height, Scene.cell_size, Scene.death_rate, Scene.gen_grid)
    
    def set_mode(self, gen_grid: bool):
        self.gen_grid = gen_grid
        self.grid.gen_grid = gen_grid