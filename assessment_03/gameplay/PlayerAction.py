from enum import Enum
from . import PlayerAction

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class PlayerAction(Enum):
    """
    Enumeration of possible player actions.
    """
    HIT = 0
    STAND = 1
    YES = 2
    NO = 3

    @staticmethod
    def get_action(action_name: str) -> PlayerAction:
        """
        Get player action for it's string representation.
        :param action_name: The action's string representation
        :return: The corresponding player action.
        """
        action_name = action_name.lower()
        if action_name == "hit":
            return PlayerAction.HIT
        elif action_name == "stand":
            return PlayerAction.STAND
        elif action_name == "yes":
            return PlayerAction.YES
        elif action_name == "no":
            return PlayerAction.NO
        else:
            return None
