from cards.CardColor import *
from cards.CardValue import *

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class Card:
    """
    A game card.
    """

    color: CardColor
    value: CardValue

    def __init__(self, color: CardColor, value: CardValue):
        """
        Constructor

        :param: color: The card's color
        :type: color: CardColor
        :param: value: The card's value
        :type: value: CardValue
        """
        self.color = color
        self.value = value
