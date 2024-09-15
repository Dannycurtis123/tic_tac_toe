'''
    library/src/tic_tac_toe/logic/models.py
'''

#region IMPORTS
from __future__ import annotations

import enum
import re

from dataclasses import dataclass
from functools import cached_property
#endregion IMPORTS

#region PLAYERMARK CLASS
class PlayerMark(enum.StrEnum):
    '''
        Define player token values
        Uses from __future__ to avoid circular import errors
    '''
    EXES = 'X'
    OHS = 'O'

    @property
    def other(self) -> PlayerMark:
        '''
            Assign player token values
        '''
        return PlayerMark.EXES if self is PlayerMark.OHS else PlayerMark.OHS
#endregion PLAYERMARK CLASS

#region GRID
@dataclass(frozen = True)
class NineByNineGrid:
    '''
        Define gamimg surface for a 9x9 grid
        Use frozen=True to lock the class in place
    '''
    cells: str = " " * 9

    def __post_init__(self) -> None:
        if not re.match(r"^[\sXO]{9}$", self.cells):
            raise ValueError("9x9 Grid can only contain 9 cells of: X, O, or space characters.")

    @cached_property
    def x_count(self) -> int:
        '''
            maintains current count of EXES
        '''
        return self.cells.count("X")

    @cached_property
    def o_count(self) -> int:
        '''
            maintains current count of OHS
        '''
        return self.cells.count("O")

    @cached_property
    def empty_count(self) -> int:
        '''
            maintains current count of Empty spaces
        '''
        return self.cells.count(" ")
#endregionGRID
