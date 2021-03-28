import random

from .Card import Card
from .CardColor import CardColor
from .CardValue import CardValue

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class Shuffle:
    """
    Shuffle machine dedicated to generate and shuffle full card decks.
    """

    _CARD_DECK_MULTIPLIER = 4

    @staticmethod
    def generate_card_deck() -> [Card]:
        """
        Generate a complete and shuffled card deck.
        :return: The generated card deck
        """

        card_deck = []

        for card_color in CardColor:
            for card_value in CardValue:
                card_deck.append(Card(card_color, card_value))

        return Shuffle.__shuffle_card_deck(card_deck * Shuffle._CARD_DECK_MULTIPLIER)

    @staticmethod
    def __shuffle_card_deck(card_deck: [Card]) -> [Card]:
        """
        Shuffle a given card deck.
        :param card_deck: The card deck to shuffle
        :return: The shuffled card deck.
        """
        shuffled_card_deck = []

        length = len(card_deck)
        while len(shuffled_card_deck) != length:
            r = random.SystemRandom()
            random_card = r.choice(card_deck)
            shuffled_card_deck.append(random_card)
            card_deck.remove(random_card)

        return shuffled_card_deck

