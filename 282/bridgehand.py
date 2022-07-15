from enum import Enum, IntEnum
from re import A
from typing import Sequence, NamedTuple, Dict, List
from copy import deepcopy
from itertools import groupby
import logging
Suit = IntEnum("Suit", list("SHDC"))
Rank = IntEnum("Rank", list("AKQJT98765432"))
logging.basicConfig(level=logging.DEBUG)


class Card(NamedTuple):
    suit: Suit
    rank: Rank


HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError()
        elif len(cards) != 13 or any((not isinstance(card, Card) for card in cards)):
            raise ValueError
        else:
            self.cards = sorted(deepcopy(cards))

    def _hand_info(self) -> Dict[Suit, List[Card]]:
        res = dict()
        for card in self.cards:
            res.setdefault(card.suit, list()).append(card)
        res = {suit: sorted(cards) for suit, cards in res.items()}
        return res

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        suit_report_list = list()
        for suit, cards in groupby(self.cards, self._suit_group_function):
            suit_report = f"{suit.name}:"
            for card in cards:
                suit_report += card.rank.name
            suit_report_list.append(suit_report)
        return " ".join(suit_report_list)

    @staticmethod
    def _suit_group_function(card: Card) -> Suit:
        return card.suit

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        return sum(HCP.get(card.rank, 0) for card in self.cards)

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        hand_dict = self._hand_info()
        return len([suit for suit in hand_dict if len(hand_dict[suit]) == 2])

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        hand_dict = self._hand_info()
        return len([suit for suit in hand_dict if len(hand_dict[suit]) == 1])

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        all_suits = set(Suit)
        suits_in_hand = set(self._hand_info().keys())
        return len(all_suits - suits_in_hand)

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        ssp_value = 0
        ssp_value += self.voids * SSP[0]
        ssp_value += self.singletons * SSP[1]
        ssp_value += self.doubletons * SSP[2]
        return ssp_value

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """

        hand_dict = self._hand_info()
        top_three_cards_in_suit = [
            hand_dict.get(suit, [])[:3] for suit in Suit]
        losing_trick_count = 0
        for top_three in top_three_cards_in_suit:
            ranks = [card.rank for card in top_three]
            logging.debug(f"Top 3 ranks: {ranks}")
            if len(top_three) == 0:
                logging.debug("Found a void")
                continue
            elif len(top_three) == 1:
                if ranks[0] != Rank.A:
                    logging.debug("Found singleton other than A")
                    losing_trick_count += 1
                else:
                    logging.debug("Found ace singleton")
                    continue
            elif len(top_three) == 2:
                if ranks[:2] == [Rank.A, Rank.K]:
                    logging.debug("Found AK doubleton")
                    continue
                elif ranks[0] in {Rank.A, Rank.K}:
                    logging.debug("Found A or K doubleton")
                    losing_trick_count += 1
                else:
                    logging.debug("Found Qx or xx doubleton")
                    losing_trick_count += 2
            else:
                assert len(top_three) == 3
                if ranks == [Rank.A, Rank.K, Rank.Q]:
                    logging.debug("Found AKQ")
                    continue
                elif ranks[:2] in [[Rank.A, Rank.K], [Rank.A, Rank.Q], [Rank.K, Rank.Q]]:
                    logging.debug("Found AKx, AQx or KQx")
                    losing_trick_count += 1
                elif ranks[0] in [Rank.A, Rank.K, Rank.Q]:
                    logging.debug("Found Axx, Kxx, or Qxx")
                    losing_trick_count += 2
                else:
                    logging.debug("Found xxx")
                    losing_trick_count += 3
        return losing_trick_count
