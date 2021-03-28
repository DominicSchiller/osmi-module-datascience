__author__ = 'Dominic Schiller'
__email__ = 'dominic.schiller@th-brandenburg.de'
__version__ = '1.0'
__license__ = 'MIT'


class Messages:
    """
    Static class listing all console prompts and messages.
    """

    # game state messages
    QUIT = "\nBlackJack has been stopped ... Have a nice day :-)"

    # input messages
    ENTER_NAME = "Please enter your name: "
    PLACE_BET = "Please place your bet (or quit by enter 0): "
    TAKE_ACTION = '\nWhat is your next action? [ hit | stand ] : '
    TAKE_ACTION_NEXT_ROUND = "\nDo you want to start a new round? [ yes | no ] : "

    # status messages
    AVAILABLE_CAPITAL = "\n{0}, you have {1}$ seed credit."
    OUT_OF_MONEY = "\n{0}, unfortunately you run out of money!\nYour game is over."

    DEALER_MUST_STAND = "\nDealer has {0} points and hence must stand.\n"
    DEALER_DRAW_CARD = "\nDealer is drawing a card ..."
    PLAYER_RECEIVES_CARD = "{0} is receiving a card ...\n"

    WON = "\nYou won! Your earnings: {0}$\n"
    WON_BY_DEALER_BUST = "\nThe dealer burst.\n" + WON
    WON_BY_BLACKJACK = "\nYou have a BLACK JACK!\nBlack Jack pays 3 to 2 - Your earnings: {0}$\n"
    LOST = "\nYou lost this round. Your loss: {0}$\n"
    LOST_BY_DEALER_BLACKJACK = "\nDealer has a BlackJack. Your loose. Your loss: {0}$\n"
    BURST = "\nYou burst and loose this round. Your loss: {0}$\n"
    STAND_OFF = "\nThis round is a stand off. You will get your bet of {0}$ back."

    # error messages
    ERR_NO_VALID_BET = "You bet is not a valid amount of $. Please try again ... \n"
    ERR_HIGHER_BET_THAN_LEFT_CAPITAL = "You tried to place a bet out of your range " \
                                       "of available capital. Please try again ...\n"
    ERR_WRONG_ACTION = "Couldn't understand your next action ..."
