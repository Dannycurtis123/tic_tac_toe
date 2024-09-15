'''
    tic_tac_toe/constants.py
    holds immutable variables used throughout the project
'''

#region IMPORTS
from dataclasses import dataclass
#endregion IMPORTS

#region CONSTANTS
@dataclass(frozen = True)
class Constants:
    '''
        Store frequently use variables to be referenced throughout the project
    '''
    #region PLAYER_DATA
    EXES = 'X'
    OHS = 'O'
    EMPTY = ' '
    #endregion PLAYER_DATA

    #region GRID_DATA
    NINE_BY_GRID = 9
    NINE_BY_WINS = ("???......"
                    "...???..."
                    "......???"
                    "?..?..?.."
                    ".?..?..?."
                    "..?..?..?"
                    "?...?...?"
                    "..?.?.?..")
    #endregion GRID_DATA

    #region REGEX
    NINE_BY_REGEX = 'r"^[\sXO]{9}$"'
    #endregion REGEX

    #region ERROR_MESSAGES
    NINE_BY_VALUE_ERR = "9x9 Grid can only contain 9 cells of: X, O, or space characters."
    #endregion ERROR_MESSAGES
#endregion CONSTANTS
