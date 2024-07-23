import itertools
import random

class Card:
    _id_counter = itertools.count(1)  # Unique ID generator

    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.id = next(Card._id_counter)

    def __repr__(self):
        return f"{self.color} {self.value}"

class Deck:
    colors = {
        2: ['Red'],
        3: ['Red', 'Blue'],
        4: ['Red', 'Blue', 'Yellow'],
        5: ['Red', 'Blue', 'Yellow', 'Black']
    }

    card_distribution = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6
    }

    def __init__(self, player_count):
        if player_count < 2 or player_count > 5:
            raise ValueError("Player count must be between 2 and 5")
        self.player_count = player_count
        self.cards = self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        deck = []
        active_colors = self.colors[self.player_count]
        for color in active_colors:
            for value, count in self.card_distribution.items():
                for _ in range(count):
                    deck.append(Card(color, value))
        return deck

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return f"Deck({len(self.cards)} cards)"

class Player:
    def __init__(self, cards_in_hand=None, movement=0):
        if cards_in_hand is None:
            cards_in_hand = []
        self.cards_in_hand = cards_in_hand
        self.movement = movement

    def __repr__(self):
        return f"Player(cards_in_hand={self.cards_in_hand}, movement={self.movement})"

# Example usage
player_count = 3
deck = Deck(player_count)
print(deck)

# Create some players and deal some cards
players = [Player() for _ in range(player_count)]

# Deal 5 cards to each player as an example
for player in players:
    player.cards_in_hand = [deck.cards.pop() for _ in range(5)]

# Print players' hands
for i, player in enumerate(players, start=1):
    print(f"Player {i}: {player}")

# Print remaining cards in deck
print(f"Remaining cards in deck: {len(deck.cards)}")

# Example of moving a card to the discard pile
discard_pile = []
discard_pile.append(players[0].cards_in_hand.pop())
print(f"Discard pile: {discard_pile}")
