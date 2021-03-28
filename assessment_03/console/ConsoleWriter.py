from entities.Dealer import Dealer

__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class ConsoleWriter:
    """
    IO class dedicated to print messages to the system's terminal/console.
    """

    CARD_LINES = [
        '┌─────────┐',
        '│{0}       │',
        '│         │',
        '│    {0}    │',
        '│ ░░░░░░░ │',
        '│      {0} │',
        '└─────────┘'
    ]

    @staticmethod
    def write_message(message: str, *args):
        """
        Print out a specific message.
        :param message: The message to print
        :param args: Arguments to insert into the message
        """
        print(message.format(*args))

    @staticmethod
    def write_cards(*players):
        """
        Print out the holding cards for all given payers in a row.
        :param players: List of players to print the holding cards for.
        """
        box_print_lines = ['', '']
        cards_print_lines = ['', '', '', '', '', '', '']

        for player in players:
            number_of_cards = len(player.hand)

            # if dealer, the first card indicates the card deck which has a hidden face
            if isinstance(player, Dealer):
                number_of_cards += 1
                card_padding_multiplier = 1
                cards_print_lines[0] += ' ' + ConsoleWriter.CARD_LINES[0]
                for i in range(1, 6):
                    cards_print_lines[i] += ' ' + ConsoleWriter.CARD_LINES[4]
                cards_print_lines[6] += ' ' + ConsoleWriter.CARD_LINES[6]

            for card in player.hand:
                cards_print_lines[0] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[0]
                cards_print_lines[1] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[1].format(card.value.symbol())
                cards_print_lines[2] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[2]
                cards_print_lines[3] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[3].format(card.color.symbol())
                cards_print_lines[4] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[2]
                cards_print_lines[5] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[5].format(card.value.symbol())
                cards_print_lines[6] += ' ' * card_padding_multiplier + ConsoleWriter.CARD_LINES[6]

            for i in range(0, len(cards_print_lines)):
                cards_print_lines[i] += '       '

            row_length = len(ConsoleWriter.CARD_LINES[0]) * number_of_cards
            name_length = len(player.name)
            box_print_lines[0] += '=' * int(((row_length/2) - 1)) + ' ' + \
                                  player.name + ' ' + \
                                  '=' * int(((row_length/2) - 1)) + '   '
            box_print_lines[1] += '=' * (row_length + name_length) + '   '

        print(box_print_lines[0])
        for line in cards_print_lines:
            print(line)
        print(box_print_lines[1])

