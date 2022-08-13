
from dataclasses import dataclass


class Grid: 
    
    grid: list

    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self._n_cols = self.width // self.cell_size
        self._n_rows = self.height // self.cell_size