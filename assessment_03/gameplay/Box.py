from entities.Dealer import Dealer
from entities.Player import Player
from cards.Shuffle import Shuffle
from gameplay.GameState import GameState
from gameplay.GameStateHandler import GameStateHandler
from gameplay.PlayerAction import PlayerAction

from console.ConsoleReader import ConsoleReader
from console.ConsoleWriter import ConsoleWriter
from console.Messages import Messages

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class Box:
    """
    The BlackJack box where the actual game takes place.
    """
    _state_handler: GameStateHandler
    _dealer: Dealer
    _player: Player

    def __init__(self):
        """
        Constructor.
        """
        self._state_handler = GameStateHandler(self)
        self._dealer = Dealer()

    @property
    def player(self):
        """
        Get the associated player.
        :return: The associated player
        """
        return self._player

    @player.setter
    def player(self, player):
        """
        Set a player to the box.
        :param player: The player to set
        """
        self._player = player
        
    @property
    def dealer(self):
        return self._dealer

    def start_game(self):
        """
        Start the boxes game.
        """
        # The game's main loop: implicit do-while loop
        while True:
            self._dealer.clear_hand()
            self._player.clear_hand()
            self._dealer.card_deck = Shuffle.generate_card_deck()

            ConsoleWriter.write_message(Messages.AVAILABLE_CAPITAL, self._player.name, str(self._player.credit))
            bet = ConsoleReader.read_bet(self._player.credit)

            if bet > 0:
                self._state_handler.bet = bet
                self._deal_cards()
            else:
                ConsoleWriter.write_message(Messages.QUIT)
                break

            self._state_handler.evaluate_game_state()

            if self._can_start_next_round():
                continue
            else:
                ConsoleWriter.write_message(Messages.QUIT)
                break

    def _deal_cards(self):
        """
        Deal cards within a round.
        """
        while True:
            self._pick_card_for_dealer()
            self._pick_card_for_player(self._player)
            ConsoleWriter.write_cards(self._dealer, self._player)

            tmp_round_status = self._state_handler.get_game_state()
            if tmp_round_status is not GameState.DEALER_BLACK_JACK and \
               tmp_round_status is not GameState.DEALER_BUST and \
               tmp_round_status is not GameState.PLAYER_BUST:
                action = ConsoleReader.read_action()
                if action == PlayerAction.HIT:
                    continue
                elif action == PlayerAction.STAND:
                    self._pick_card_for_dealer()
                    ConsoleWriter.write_cards(self._dealer, self._player)
                    break
            else:
                break

    def _pick_card_for_dealer(self):
        """
        Pick a dealer's card.
        """
        if not self._dealer.hand_sum >= 17:
            ConsoleWriter.write_message(Messages.DEALER_DRAW_CARD)
            self._dealer.draw_card_for(self._dealer)
        else:
            ConsoleWriter.write_message(Messages.DEALER_MUST_STAND, self._dealer.hand_sum)

    def _pick_card_for_player(self, player: Player):
        """
        Pick a card from the dealer's deck and associated it to a specific user.
        :param player: The player which will retrieve the picked card
        """
        ConsoleWriter.write_message(Messages.PLAYER_RECEIVES_CARD, self._player.name)
        self._dealer.draw_card_for(player)

    def _can_start_next_round(self) -> bool:
        """
        Determine whether the user will and is able to continue with a further round.
        :return: The proceed status
        """
        action = ConsoleReader.read_action(Messages.TAKE_ACTION_NEXT_ROUND)
        if action is PlayerAction.YES:
            if self._player.credit <= 0:
                ConsoleWriter.write_message(Messages.OUT_OF_MONEY, self._player.name)
                ConsoleWriter.write_message(Messages.QUIT)
                return False
            else:
                return True
        else:
            return False
