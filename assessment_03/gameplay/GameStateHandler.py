from .GameState import GameState
from console.ConsoleWriter import ConsoleWriter
from console.Messages import Messages


class GameStateHandler:
    """
    Handler class dedicated to determine and evaluate the game state from the associated blackjack box.
    """
    _bet: int

    def __init__(self, box):
        """
        Constructor
        :param box: The Blackjack box to handle the state for
        """
        self._bet = 0
        self._box = box

    @property
    def bet(self):
        """
        Get the currently placed bet.
        :return: The currently placed bet
        """
        return self._bet

    @bet.setter
    def bet(self, new_bet):
        """
        Place the bet for the current round.
        :param new_bet: The bet to place
        """
        self._bet = new_bet

    def get_game_state(self) -> GameState:
        """
        Determines the current round's game status.
        :return: The current round's game status
        """
        # (1) check if Player has a blackjack
        if self._box.player.hand_sum == 21:
            return GameState.PLAYER_BLACK_JACK

        # (2) check if player burst
        elif self._box.player.hand_sum > 21:
            return GameState.PLAYER_BUST

        # (3) check if the dealer has a black jack
        elif self._box.dealer.hand_sum == 21:
            return GameState.DEALER_BLACK_JACK

        # (4) check if dealer bust
        elif self._box.dealer.hand_sum > 21:
            return GameState.DEALER_BUST

        # (5) check if player is ahead
        elif self._box.player.hand_sum > self._box.dealer.hand_sum:
            return GameState.PLAYER_AHEAD

        # (6) check if dealer is ahead
        elif self._box.dealer.hand_sum > self._box.player.hand_sum:
            return GameState.DEALER_AHEAD

        # (7) dealer and player are stand off
        else:
            return GameState.STAND_OFF

    def evaluate_game_state(self):
        """
        Evaluate the current round's final game status.
        """
        round_status = self.get_game_state()
        if round_status is GameState.DEALER_AHEAD:
            self._box.player.credit -= self._bet
            ConsoleWriter.write_message(Messages.LOST, self._bet)

        elif round_status is GameState.DEALER_BLACK_JACK:
            self._box.player.credit -= self._bet
            ConsoleWriter.write_message(Messages.LOST_BY_DEALER_BLACKJACK, self._bet)

        elif round_status is GameState.PLAYER_BUST:
            self._box.player.credit -= self._bet
            ConsoleWriter.write_message(Messages.BURST, self._bet)

        elif round_status is GameState.PLAYER_AHEAD:
            self._box.player.credit += self._bet
            ConsoleWriter.write_message(Messages.WON, str(self._bet))

        elif round_status is GameState.DEALER_BUST:
            self._box.player.credit += self._bet
            ConsoleWriter.write_message(Messages.WON_BY_DEALER_BUST, str(self._bet))

        elif round_status is GameState.PLAYER_BLACK_JACK:
            self._bet *= 1.5
            self._box.player.credit += self._bet
            ConsoleWriter.write_message(Messages.WON_BY_BLACKJACK, str(self._bet))

        elif round_status is GameState.STAND_OFF:
            self._box.player.credit += self._bet
            ConsoleWriter.write_message(Messages.STAND_OFF, str(self._bet))
