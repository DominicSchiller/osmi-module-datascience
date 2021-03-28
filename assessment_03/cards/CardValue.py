from enum import Enum

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class CardValue(Enum):
    """
    Enumeration of game card values.
    """

    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12

    def value(self):
        """
        Get the card value's numeric representation.
        :return card value's numeric representation
        """
        if self == CardValue.TWO:
            return 2
        elif self == CardValue.THREE:
            return 3
        elif self == CardValue.FOUR:
            return 4
        elif self == CardValue.FIVE:
            return 5
        elif self == CardValue.SIX:
            return 6
        elif self == CardValue.SEVEN:
            return 7
        elif self == CardValue.EIGHT:
            return 8
        elif self == CardValue.NINE:
            return 9
        elif self == CardValue.TEN:
            return 10
        elif self == CardValue.JACK:
            return 10
        elif self == CardValue.QUEEN:
            return 10
        elif self == CardValue.KING:
            return 10
        elif self == CardValue.ACE:
            return 11
        else:
            return 0

    def symbol(self):
        """
        Get the card value's symbolic representation.
        :return card value's symbolic representation
        """
        if self == CardValue.JACK:
            return ' J'
        elif self == CardValue.QUEEN:
            return ' Q'
        elif self == CardValue.KING:
            return ' K'
        elif self == CardValue.ACE:
            return ' A'
        elif self == CardValue.TEN:
            return str(self.value())
        else:
            return ' ' + str(self.value())
