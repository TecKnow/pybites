from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()
SUIT_NAMES = (["0"] + "1 2 3 4 5 6 7 8 9".split() * 2 +
              ["Draw Two", "Skip", "Reverse"] * 2)
WILD_NAMES = ["Wild"]*4 + ["Wild Draw Four"]*4

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    suit_cards = [UnoCard(suit, name) for suit in SUITS for name in SUIT_NAMES]
    wild_cards = [UnoCard(None, name) for name in WILD_NAMES]
    uno_deck = suit_cards + wild_cards
    return uno_deck


if __name__ == "__main__":
    create_uno_deck()
