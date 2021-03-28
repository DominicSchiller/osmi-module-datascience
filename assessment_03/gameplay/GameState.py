from enum import Enum

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class GameState(Enum):
    """
    Enumeration of status which can occur within a black jack game round.
    """

    IN_PROGRESS = 1

    PLAYER_AHEAD = 2
    PLAYER_BUST = 3
    PLAYER_BLACK_JACK = 4

    DEALER_AHEAD = 5
    DEALER_BUST = 6
    DEALER_BLACK_JACK = 7

    STAND_OFF = 8
