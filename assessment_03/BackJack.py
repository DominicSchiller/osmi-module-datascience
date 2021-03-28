from console.ConsoleReader import ConsoleReader
from entities.Player import Player
from gameplay.Box import Box

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'

# The Game's major entry point.

# init player and game box
player = Player(ConsoleReader.read_name())
box = Box()
box.player = player

# start the boxes game
box.start_game()
