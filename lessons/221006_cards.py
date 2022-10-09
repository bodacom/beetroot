"""
Instructions:

Fill in the methods of the Deck class to produce the same printed results
as in the comments below. Good luck, and have fun!
"""

from __future__ import annotations

import random

from typing import Dict, List, Tuple


class Deck:
    """
    We want to play Durak, so create the deck and give us the cards.
    """

    def __init__(self, suits: Tuple[str], ranks: Tuple[str]):
        """
        Init a deck of cards.
        """
        # ** Your code here **

    def shuffle(self) -> None:
        """
        Randomly shuffle a deck.
        """
        # ** Your code here **

    def __str__(self):
        """
        A string representation of the cards.
        """
        # ** Your code here **


suits = ("♣", "♥", "♠", "♦")
ranks = ("6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

deck = Deck(suits, ranks)

print(f"Current deck of cards:\n{deck.cards}")

# Current deck of cards:
# [{'rank': '6', 'suit': '♣'}, {'rank': '7', 'suit': '♣'}, {'rank': '8', 'suit': '♣'}, {'rank': '9', 'suit': '♣'}, {'rank': '10', 'suit': '♣'},{'rank': 'Jack', 'suit': '♣'},
# {'rank': 'Queen', 'suit': '♣'}, {'rank': 'King', 'suit': '♣'}, {'rank': 'Ace', 'suit': '♣'}, {'rank': '6', 'suit': '♥'},{'rank': '7', 'suit': '♥'}, {'rank': '8', 'suit': '♥'},
# {'rank': '9', 'suit': '♥'}, {'rank': '10', 'suit': '♥'}, {'rank': 'Jack', 'suit': '♥'}, {'rank': 'Queen', 'suit': '♥'}, {'rank': 'King', 'suit': '♥'}, {'rank': 'Ace', 'suit': '♥'},
# {'rank': '6', 'suit': '♠'}, {'rank': '7', 'suit': '♠'}, {'rank': '8', 'suit': '♠'},{'rank': '9', 'suit': '♠'}, {'rank': '10', 'suit': '♠'}, {'rank': 'Jack', 'suit': '♠'},
# {'rank': 'Queen', 'suit': '♠'}, {'rank': 'King', 'suit': '♠'}, {'rank': 'Ace', 'suit': '♠'}, {'rank': '6', 'suit': '♦'}, {'rank': '7', 'suit': '♦'}, {'rank': '8', 'suit': '♦'},
# {'rank': '9', 'suit': '♦'},{'rank': '10', 'suit': '♦'}, {'rank': 'Jack', 'suit': '♦'}, {'rank': 'Queen', 'suit': '♦'}, {'rank': 'King', 'suit': '♦'}, {'rank': 'Ace', 'suit': '♦'}]

print(deck)

# 6♣
# 7♣
# 8♣
# 9♣
# 10♣
# Jack♣
# Queen♣
# King♣
# Ace♣
# 6♥
# 7♥
# 8♥
# 9♥
# 10♥
# Jack♥
# Queen♥
# King♥
# Ace♥
# 6♠
# 7♠
# 8♠
# 9♠
# 10♠
# Jack♠
# Queen♠
# King♠
# Ace♠
# 6♦
# 7♦
# 8♦
# 9♦
# 10♦
# Jack♦
# Queen♦
# King♦
# Ace♦

deck.shuffle()

print(f"Shuffeld deck of cards:\n{deck.cards}")

# Shuffeld deck of cards:
# [{'rank': 'Queen', 'suit': '♠'}, {'rank': 'Jack', 'suit': '♠'}, {'rank': 'Jack', 'suit': '♣'}, {'rank': 'Ace', 'suit': '♥'}, {'rank': 'Ace', 'suit': '♣'}, {'rank': '7', 'suit': '♥'},
# {'rank': '8', 'suit': '♦'}, {'rank': '7', 'suit': '♠'}, {'rank': 'Jack', 'suit': '♥'}, {'rank': '8', 'suit': '♥'}, {'rank': '6', 'suit': '♣'}, {'rank': '9', 'suit': '♣'},
# {'rank': 'Ace', 'suit': '♦'}, {'rank': 'Queen', 'suit': '♥'}, {'rank': '7', 'suit': '♣'}, {'rank': 'King', 'suit': '♠'}, {'rank': '8', 'suit': '♣'}, {'rank': 'King', 'suit': '♥'},
# {'rank': 'Queen', 'suit': '♣'}, {'rank': '9', 'suit': '♦'}, {'rank': '10', 'suit': '♣'}, {'rank': '6', 'suit': '♦'}, {'rank': 'Jack', 'suit': '♦'}, {'rank': 'Queen', 'suit': '♦'},
# {'rank': '6', 'suit': '♠'}, {'rank': '10', 'suit': '♠'}, {'rank': '9', 'suit': '♠'}, {'rank': '6', 'suit': '♥'}, {'rank': '8', 'suit': '♠'}, {'rank': 'King', 'suit': '♦'},
# {'rank': '10', 'suit': '♦'}, {'rank': '7', 'suit': '♦'}, {'rank': 'King', 'suit': '♣'}, {'rank': '9', 'suit': '♥'}, {'rank': '10', 'suit': '♥'}, {'rank': 'Ace', 'suit': '♠'}]

print(deck)

# Queen♠
# Jack♠
# Jack♣
# Ace♥
# Ace♣
# 7♥
# 8♦
# 7♠
# Jack♥
# 8♥
# 6♣
# 9♣
# Ace♦
# Queen♥
# 7♣
# King♠
# 8♣
# King♥
# Queen♣
# 9♦
# 10♣
# 6♦
# Jack♦
# Queen♦
# 6♠
# 10♠
# 9♠
# 6♥
# 8♠
# King♦
# 10♦
# 7♦
# King♣
# 9♥
# 10♥
# Ace♠


жесть
