import random
from typing import Tuple
class Deck:
    """
    We want to play BlackJack, so create the deck and give us the cards.
    """

    def __init__(self, suits: Tuple[str], ranks: Tuple[str]):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self) -> None:
        """
        Randomly shuffle a deck.
        """
        random.shuffle(self.cards)

    def __str__(self):
        """
        A string representation of the cards.
        """
        deck = ""
        for card in self.cards:
            deck += str(card) + "\n"

        return deck

    def __repr__(self):
        return f"{[card for card in self.cards]}"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator > len(self.cards) - 1:
            raise StopIteration
        card = self.cards[self.iterator]
        self.iterator += 1
        return card 



class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __int__(self):
        return int(self.cards_weights[self.rank])


deck = Deck(("♣", "♥", "♠", "♦"), ("6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"))
deck.shuffle()


for card in deck:
    print(card)


class Fibbonachi:
    def __iter__(self):
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        tmp = self.next_val
        self.next_val += self.cur_val  # next_val = 1 + 1 = 2
        self.cur_val = tmp
        return tmp


class MySquaredNums:
    def __init__(self, i, to_i, step):
        self.i = i
        self.to_i = to_i
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.to_i:
            raise StopIteration
        val = self.i ** 2
        self.i += self.step
        return val
