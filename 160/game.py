from csv import DictReader
import os
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_map = dict()
    for row in DictReader(open(BATTLE_DATA, 'r', newline='')):
        defeat_map[row["Attacker"]] = [
            move for (move, outcome) in row.items() if outcome == "win"]
    return defeat_map


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if player1 not in defeat_mapping.keys() or player2 not in defeat_mapping.keys():
        raise ValueError(
            f"{player1 if player1 not in defeat_mapping.keys() else player2} is not a valid attack")
    elif player2 in defeat_mapping[player1]:
        return player1
    elif player1 in defeat_mapping[player2]:
        return player2
    elif player1 == player2:
        return "Tie"
    else:
        raise Exception("Well, that's not reasonably possible.")
