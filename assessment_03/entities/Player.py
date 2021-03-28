from cards.Card import Card

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class Player(object):
    """
    Represents a player.
    """
    _name: str
    _hand: [Card]
    _credit: int

    def __init__(self, name: str):
        """
        Constructor.
        :param name: The player's name
        """
        self._name = name
        self._hand = []
        self._credit = 100

    @property
    def name(self):
        """
        Get the player's name.
        :return:
        """
        return self._name

    @property
    def hand(self):
        """
        Get the list of all currently holding cards.
        :return: The list of all currently holding cards.
        """
        return self._hand

    @property
    def hand_sum(self):
        """
        Get the sum of all numeric values from each holding card.
        :return: The sum of all numeric values from each holding card
        """
        sum = 0
        for card in self._hand:
            sum += card.value.value()
        return sum

    @property
    def credit(self):
        """
        Get the player's current credit.
        :return: The player's current credit.
        """
        return self._credit

    @credit.setter
    def credit(self, credit_update: int):
        """
        Set the player's available credit.
        :param credit_update: The credit update to apply
        """
        self._credit = credit_update

    def clear_hand(self):
        """
        Clears the list of currently holding cards.
        """
        self._hand = []

