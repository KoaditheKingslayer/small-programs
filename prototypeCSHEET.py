import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import json

class CharacterSheetApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Character Sheet")

        # Character information
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.player_label = tk.Label(master, text="Player:")
        self.player_label.grid(row=1, column=0, padx=10, pady=5)
        self.player_entry = tk.Entry(master)
        self.player_entry.grid(row=1, column=1, padx=10, pady=5)

        # Stats
        self.stats_label = tk.Label(master, text="Stats:")
        self.stats_label.grid(row=2, column=0, padx=10, pady=5)

        stats = ["Mental", "Social", "Physical", "Spirit", "Hearthfire", "Health"]
        self.stat_vars = {stat: tk.StringVar() for stat in stats}
        self.stat_labels = {stat: tk.Label(master, text=stat) for stat in stats}
        self.stat_dropdowns = {stat: ttk.Combobox(master, textvariable=self.stat_vars[stat], values=list(range(1, 16))) for stat in stats}

        for i, stat in enumerate(stats):
            self.stat_labels[stat].grid(row=2 + i, column=0, padx=10, pady=5)
            self.stat_dropdowns[stat].grid(row=2 + i, column=1, padx=10, pady=5)

        # Save and Load buttons
        self.save_button = tk.Button(master, text="Save", command=self.save_character)
        self.save_button.grid(row=0, column=2, padx=10, pady=10)

        self.load_button = tk.Button(master, text="Load", command=self.load_character_window)
        self.load_button.grid(row=1, column=2, padx=10, pady=10)

    def save_character(self):
        character_data = {
            "Name": self.name_entry.get(),
            "Player": self.player_entry.get(),
            "Stats": {stat: int(self.stat_vars[stat].get()) for stat in self.stat_vars}
        }

        existing_characters = self.load_all_characters()
        existing_characters[character_data["Name"]] = character_data

        with open("characters.json", "w") as json_file:
            json.dump(existing_characters, json_file, indent=2)

        print("Character saved:", character_data)

    def load_character_window(self):
        characters = self.load_all_characters()
        character_names = list(characters.keys())

        if character_names:
            load_window = tk.Toplevel(self.master)
            load_window.title("Load Character")

            listbox = tk.Listbox(load_window)
            for name in character_names:
                listbox.insert(tk.END, name)

            listbox.pack()

            select_button = tk.Button(load_window, text="Select", command=lambda: self.load_character(listbox.get(tk.ACTIVE), load_window))
            select_button.pack()

        else:
            print("No characters found.")

    def load_character(self, character_name, load_window):
        characters = self.load_all_characters()

        if character_name in characters:
            character_data = characters[character_name]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, character_data["Name"])

            self.player_entry.delete(0, tk.END)
            self.player_entry.insert(0, character_data["Player"])

            for stat, var in self.stat_vars.items():
                # Assign a default value of 1 if the stat is missing in the loaded character data
                var.set(character_data["Stats"].get(stat, 1))

            print(f"Character '{character_name}' loaded.")
            load_window.destroy()
        else:
            print(f"Character '{character_name}' not found.")

    def load_all_characters(self):
        try:
            with open("characters.json", "r") as json_file:
                characters = json.load(json_file)
        except FileNotFoundError:
            characters = {}

        return characters

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()
