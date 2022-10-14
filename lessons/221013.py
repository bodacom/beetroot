# class New():

#     def __init__(self) -> None:
#         print('hello')
#     # def __new__(cls):
#     #     print('new instance')

# obj_new = New()

# class Time:

#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes

#     def __gt__(self, other):
#         if self.hours > other.hours:
#             return True
#         elif self.hours < other.hours:
#             return False
#         else:
#             if self.minutes > other.minutes:
#                 return True
#             else:
#                 return False


# dinner_time = Time(9, 20)
# lunch_time = Time(9, 20)

# print(dinner_time > lunch_time)  # True


class Card:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    # def __repr__(self):
    #     return f"Card({self.name}, {self.suit})"


clubs_queen = Card("Queen", "Clubs")
diamonds_queen = Card("Queen", "Diamonds")

deck = []
deck.append(clubs_queen)
deck.append(diamonds_queen)

print(deck)  # [Card("Queen", "Clubs"), Card("Queen", "Diamonds")] __repr__
