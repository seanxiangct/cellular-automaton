import random
import pygame

class Cell(pygame.Rect):

    def __init__(self, x, y, cell_size, death_rate=0.05, state=0):
        super().__init__(x, y, cell_size, cell_size)
        self.x = x
        self.y = y
        self.i_x = self.x // cell_size
        self.i_y = self.y // cell_size
        self.death_rate = death_rate
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

    def update(self, env: int):
        '''
        update rule: 
        1. if the current cell is alive, and has less than 2 neighbours, it dies
        2. if the current cell is alive, and has more than 3 neighbours, it dies
        3. 
        '''
        if self.state == 1 and (env < 2 or env > 3):
            self.state = 0
        elif self.state == 0 and env == 3:
            self.state = 1
        elif random.random() < self.death_rate:
            self.state = 0
        return self.state
    
    def __str__(self) -> str:
        return super().__str__()