'''
    library/src/tic_tac_toe/logic/models.py
'''

#region IMPORTS
from __future__ import annotations
import enum
from dataclasses import dataclass
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

#endregionGRID
