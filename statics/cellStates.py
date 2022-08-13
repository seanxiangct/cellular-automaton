from dataclasses import dataclass


from enum import Enum

class CellStates(Enum):
    '''
    Value of states indicates their generation probability.
    '''
    LIVE = 0.1
    DEAD = 0.9