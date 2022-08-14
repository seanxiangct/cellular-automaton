import random
import pygame

from .cell import Cell
from statics.cellStates import CellStates
from statics.colours import Colours

class Grid: 
    
    def __init__(self, display, width, height, cell_size=10, death_rate=0.05, gen_grid=False):
        '''
        populate grid with cells
        '''
        self.display = display
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self._n_cols = self.width // self.cell_size
        self._n_rows = self.height // self.cell_size
        self.death_rate = death_rate
        self.gen_grid = gen_grid
        # self.grid = self.draw_grid()
        self._grid = []

    def draw_grid(self):

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
            self._grid.append(row)
        return self._grid

    def update_grid(self):

        # TODO: optimization
        new_grid = self._grid
        for row in self._grid:
            for cell in row:
                neighbours = cell.get_neighbours(self._grid)
                life_count = 0
                for n in neighbours:
                    if n.state == 1:
                        life_count += 1
                new_state = cell.update(life_count)
                new_grid[cell.i_x][cell.i_y].state = new_state
                if new_state:
                    pygame.draw.rect(self.display, Colours.green_clr, cell)
                else:
                    pygame.draw.rect(self.display, Colours.white_clr, cell)
        self._grid = new_grid
        return self._grid
    
    def activate_cell(self, pix_x, pix_y):
    # find the nearest cell on the grid
        for row in self._grid:
            for cell in row:
                if cell.collidepoint(pix_x, pix_y):
                    cell.state = 1
                    pygame.draw.rect(self.display, Colours.green_clr, cell)

                    break