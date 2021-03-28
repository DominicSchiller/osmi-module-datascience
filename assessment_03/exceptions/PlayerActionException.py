__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class PlayerActionException(Exception):
    """
    Exception which should be raised when the player entered a wrong (spelled) action.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        :param args:
        :param kwargs:
        """
        Exception.__init__(self, *args, **kwargs)