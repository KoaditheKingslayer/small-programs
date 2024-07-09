import tkinter as tk
from tkinter import messagebox
import random

class WarGame:
    def __init__(self, master):
        self.master = master
        self.master.title("War Card Game")

        self.deck = self.initialize_deck()
        self.discard_pile = []
        self.player_hand = self.draw_hand(5)
        self.computer_hand = self.draw_hand(5)

        self.create_widgets()

    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def draw_hand(self, num_cards):
        hand = [self.deck.pop() for _ in range(num_cards)]
        return hand

    def compare_cards(self, player_card, computer_card):
        rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        player_rank_index = rank_order.index(player_card['rank'])
        computer_rank_index = rank_order.index(computer_card['rank'])
        return player_rank_index - computer_rank_index

    def play_battle(self, selected_card_index):
        player_card = self.player_hand.pop(selected_card_index)
        computer_card = random.choice(self.computer_hand)

        result = self.compare_cards(player_card, computer_card)

        if result > 0:
            self.player_hand.append(computer_card)
            self.discard_pile.extend([player_card, computer_card])
            self.display_result("Player wins the battle!")
        elif result < 0:
            self.computer_hand.remove(computer_card)
            self.player_hand.append(player_card)
            self.discard_pile.extend([player_card, computer_card])
            self.display_result("Computer wins the battle!")
        else:
            self.discard_pile.extend([player_card, computer_card])
            self.display_result("It's a tie!")

        if not self.deck and not self.discard_pile:
            self.game_over()

    def display_result(self, message):
        self.result_label.config(text=message)

    def game_over(self):
        if not self.player_hand:
            messagebox.showinfo("Game Over", "Player runs out of cards. Computer wins!")
        else:
            messagebox.showinfo("Game Over", "Computer runs out of cards. Player wins!")
        self.master.destroy()

    def create_widgets(self):
        self.result_label = tk.Label(self.master, text="", font=('Helvetica', 12))
        self.result_label.pack(pady=10)

        self.cards_frame = tk.Frame(self.master)
        self.cards_frame.pack()

        for i, card in enumerate(self.player_hand):
            card_button = tk.Button(self.cards_frame, text=f"{card['rank']} of {card['suit']}",
                                    command=lambda i=i: self.play_battle(i))
            card_button.grid(row=0, column=i, padx=5)

def main():
    root = tk.Tk()
    game = WarGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
