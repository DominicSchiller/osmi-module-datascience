from .Player import Player
from cards.Card import Card

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class Dealer(Player):
    """
    Represents the BlackJack dealer.
    """

    _card_deck: [Card]

    def __init__(self):
        """
        Constructor.
        """
        super(Dealer, self).__init__("Dealer")
        self._card_deck = []
        self._credit = 50000

    @property
    def card_deck(self):
        """
        Get the dealer's card deck.
        :return: The dealer's card deck
        """
        return self._card_deck

    @card_deck.setter
    def card_deck(self, new_card_deck):
        """
        Set the dealer's card deck.
        :param new_card_deck: The new card deck to apply.
        """
        self._card_deck = new_card_deck

    def draw_card_for(self, player: Player):
        """
        Draw a card and assign it to a specific player.
        :param player: The player to assign the card to
        """
        card = self._card_deck[0]
        self._card_deck.remove(card)
        player.hand.append(card)
