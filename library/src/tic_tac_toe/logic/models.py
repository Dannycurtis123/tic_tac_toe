'''
    library/src/tic_tac_toe/logic/models.py
'''

#region IMPORTS
from __future__ import annotations

import enum
import re

from dataclasses import dataclass
from functools import cached_property
from constants import Constants
#endregion IMPORTS

#region PLAYERMARK CLASS
class PlayerMark(enum.StrEnum):
    '''
        Define player token values
        Uses from __future__ to avoid circular import errors
    '''
    EXES = Constants.EXES
    OHS = Constants.OHS

    @property
    def other(self) -> PlayerMark:
        '''
            Assign player token values
        '''
        return PlayerMark.EXES if self is PlayerMark.OHS else PlayerMark.OHS
#endregion PLAYERMARK CLASS

#region NINE_BY_NINE_GRID
@dataclass(frozen = True)
class NineByNineGrid:
    '''
        Define gamimg surface for a 9x9 grid
        Use frozen=True to lock the class in place
    '''
    cells: str = Constants.EMPTY * Constants.NINE_BY_GRID

    def __post_init__(self) -> None:
        if not re.match(Constants.NINE_BY_REGEX, self.cells):
            raise ValueError(Constants.NINE_BY_VALUE_ERR)

    @cached_property
    def x_count(self) -> int:
        '''
            maintains current count of EXES
        '''
        return self.cells.count(Constants.EXES)

    @cached_property
    def o_count(self) -> int:
        '''
            maintains current count of OHS
        '''
        return self.cells.count(Constants.OHS)

    @cached_property
    def empty_count(self) -> int:
        '''
            maintains current count of Empty spaces
        '''
        return self.cells.count(Constants.EMPTY)
#endregion NINE_BY_NINE_GRID

#region PLAYER_MOVE
@dataclass(frozen = True)
class PlayerMove:
    '''
        Holds player move information
        Use frozen=True to lock the class in place    
    '''
    player_mark = PlayerMark
    cell_index = int
    before_state = GameState
    after_state = GameState
#region PLAYER_MOVE

#region GAMESTATE
@dataclass(frozen = True)
class GameState:
    '''
        Holds player move information
        Use frozen=True to lock the class in place    
    '''
    grid: NineByNineGrid
    starting_mark: PlayerMark = PlayerMark(Constants.EXES)

    @cached_property
    def current_mark(self) -> PlayerMark:
        '''
            placeholder
        '''
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other

    @cached_property
    def game_not_started(self) -> bool:
        '''
            if all cells are empty then game has not started
        '''
        return self.grid.empty_count == 9

    @cached_property
    def game_over(self) -> bool:
        '''
            game ends without either player winning or tying
        '''
        return self.winner is not None or self.tie

    @cached_property
    def tie(self) -> bool:
        '''
            placeholder
        '''
        return self.winner is None and self.grid.empty_count == 0

    @cached_property
    def winner(self) -> PlayerMark | None:
        '''
            loop through pattern to find winning match to see if there is a winner
        '''
        for pattern in Constants.NINE_BY_WINS:
            for mark in PlayerMark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None

    @cached_property
    def winning_cells(self) -> list[int]:
        '''
            list the winning cells to show them different visually
        '''
        for pattern in Constants.NINE_BY_WINS:
            for mark in PlayerMark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [match.start()
                            for match in re.finditer(r"\?", pattern)]
        return []
#region GAMESTATE
