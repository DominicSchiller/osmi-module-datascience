from exceptions.CreditException import CreditException
from exceptions.PlayerActionException import PlayerActionException
from .Messages import Messages
from gameplay.PlayerAction import PlayerAction

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class ConsoleReader:
    """
    IO class dedicated to read inputs from the system's console/terminal.
    """

    @staticmethod
    def read_bet(credit_left: int) -> int:
        """
        Prompt and read a player's bet.
        :param credit_left: The player's left credit to choose a bet from
        :return: The placed bet
        """
        try:
            bet = int(input(Messages.PLACE_BET))
            if bet > credit_left:
                raise CreditException
            else:
                return bet
        except ValueError:
            print(Messages.ERR_NO_VALID_BET)
            return ConsoleReader.read_bet(credit_left)
        except CreditException:
            print(Messages.ERR_HIGHER_BET_THAN_LEFT_CAPITAL)
            return ConsoleReader.read_bet(credit_left)

    @staticmethod
    def read_name():
        """
        Prompt and read a player's name.
        :return: The entered name
        """
        return input(Messages.ENTER_NAME)

    @staticmethod
    def read_action(message=Messages.TAKE_ACTION) -> PlayerAction:
        """
        Prompt and rad a player's action.
        :param message: The prompt message for requesting the action
        :return: The entered action
        """
        action = PlayerAction.get_action(input(message))

        try:
            if action is None:
                raise PlayerActionException
            else:
                return action
        except PlayerActionException:
            print(Messages.ERR_WRONG_ACTION)
            ConsoleReader.read_action()
