from enum import Enum

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class CardColor(Enum):
    """
    Enumeration of game card colors.
    """

    DIAMONDS = 0
    HEARTS = 1
    CLUBS = 2
    SPADES = 3

    def symbol(self):
        """
        Get the symbolic representation of the card's color.
        :return: the symbolic representation of the card's color
        """
        if self == CardColor.DIAMONDS:
            return '♦'
        elif self == CardColor.HEARTS:
            return '♥'
        elif self == CardColor.CLUBS:
            return '♠'
        elif self == CardColor.SPADES:
            return '♣'
        else:
            return ''
