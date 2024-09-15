'''
    library/src/tic_tac_toe/logic/models.py
'''

#region IMPORTS
from __future__ import annotations
import enum
#endregion IMPORTS

#region CLASS
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
#endregion CLASS
