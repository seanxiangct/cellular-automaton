import random
import pygame

from .cell import Cell
from statics.cellStates import CellStates
from statics.colours import Colours

# TODO: fix importshttps://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912

class Grid: 
    
    def __init__(self, display, width, height, cell_size=10, death_rate=0.05, gen_grid=False):
        self.display = display
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self._n_cols = self.width // self.cell_size
        self._n_rows = self.height // self.cell_size
        self.death_rate = death_rate
        self.gen_grid = gen_grid
        self.grid = self.draw_grid()

    def draw_grid(self):

        grid = []
        x_cor = 0
        y_cor = 0
        for j in range(self._n_cols):
            row = []
            for i in range(self._n_rows):
                cell = None
                if self.gen_grid:
                    rand_state = random.choices(population=list(CellStates), weights=[CellStates.LIVE.value, CellStates.DEAD.value])[0]
                    cell = Cell(x_cor + j * self.cell_size, y_cor + i * self.cell_size, self.cell_size, self.death_rate, rand_state)
                else:
                    cell = Cell(x_cor + j * self.cell_size, y_cor + i * self.cell_size, self.cell_size, self.death_rate, 0)
                row.append(cell)
                pygame.draw.rect(self.display, Colours.white_clr, cell)
            grid.append(row)
        return grid