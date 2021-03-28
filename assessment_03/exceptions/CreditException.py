__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class CreditException(Exception):
    """
    Exception which should be raised when the player exceeded his credit boundary.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor.
        :param args:
        :param kwargs:
        """
        Exception.__init__(self, *args, **kwargs)
