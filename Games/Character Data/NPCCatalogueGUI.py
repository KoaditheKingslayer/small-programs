import json
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class NPC:
    def __init__(self, name, race, role, stats, armor_class, attacks, hit_points, abilities, equipment):
        self.name = name
        self.race = race
        self.role = role
        self.stats = stats
        self.armor_class = armor_class
        self.attacks = attacks
        self.hit_points = hit_points
        self.abilities = abilities
        self.equipment = equipment

    def to_dict(self):
        return {
            'name': self.name,
            'race': self.race,
            'role': self.role,
            'stats': self.stats,
            'armor_class': self.armor_class,
            'attacks': self.attacks,
            'hit_points': self.hit_points,
            'abilities': self.abilities,
            'equipment': self.equipment
        }

    @staticmethod
    def from_dict(data):
        return NPC(
            data['name'], data['race'], data['role'], data['stats'],
            data['armor_class'], data['attacks'], data['hit_points'],
            data['abilities'], data['equipment']
        )

class NPCCatalog:
    def __init__(self, filepath='npc_catalog.json'):
        self.filepath = filepath
        self.npcs = self.load_npcs()

    def load_npcs(self):
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return [NPC.from_dict(npc) for npc in data]
        except FileNotFoundError:
            return []

    def save_npcs(self):
        with open(self.filepath, 'w') as file:
            json.dump([npc.to_dict() for npc in self.npcs], file, indent=4)

    def add_npc(self, npc):
        self.npcs.append(npc)
        self.save_npcs()

    def update_npc(self, npc):
        for i, existing_npc in enumerate(self.npcs):
            if existing_npc.name == npc.name:
                self.npcs[i] = npc
                self.save_npcs()
                return

    def get_npc(self, name):
        return next((npc for npc in self.npcs if npc.name == name), None)

class NPCApp:
    def __init__(self, root):
        self.catalog = NPCCatalog()
        self.root = root
        self.root.title("NPC Catalog")
        
        self.tree = ttk.Treeview(root, columns=('Race', 'Role'), show='headings')
        self.tree.heading('Race', text='Race')
        self.tree.heading('Role', text='Role')
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.load_tree()
        
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.X, expand=False)
        
        tk.Button(btn_frame, text="Add NPC", command=self.add_npc).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="View NPC", command=self.view_npc).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Edit NPC", command=self.edit_npc).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Refresh", command=self.load_tree).pack(side=tk.LEFT, padx=5, pady=5)

    def load_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for npc in self.catalog.npcs:
            self.tree.insert('', 'end', iid=npc.name, values=(npc.race, npc.role))

    def add_npc(self):
        npc_data = self.prompt_npc_data()
        if npc_data:
            npc = NPC(**npc_data)
            self.catalog.add_npc(npc)
            self.load_tree()

    def view_npc(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "No NPC selected.")
            return
        npc_name = selected[0]
        npc = self.catalog.get_npc(npc_name)
        if npc:
            self.show_npc_window(npc)
        else:
            messagebox.showinfo("Info", "NPC not found.")

    def edit_npc(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "No NPC selected.")
            return
        npc_name = selected[0]
        npc = self.catalog.get_npc(npc_name)
        if npc:
            npc_data = self.prompt_npc_data(npc)
            if npc_data:
                updated_npc = NPC(**npc_data)
                self.catalog.update_npc(updated_npc)
                self.load_tree()

    def show_npc_window(self, npc):
        npc_window = tk.Toplevel(self.root)
        npc_window.title(f"NPC: {npc.name}")
        npc_window.geometry("1000x600")
        npc_window.resizable(True, True)

        info = f"""
        Name: {npc.name}
        Race: {npc.race}
        Role: {npc.role}
        Stats: {npc.stats}
        Armor Class: {npc.armor_class}
        Attacks: {npc.attacks}
        Hit Points: {npc.hit_points}
        Abilities: {npc.abilities}
        Equipment: {npc.equipment}
        """

        label = tk.Label(npc_window, text=info, justify=tk.LEFT, padx=10, pady=10, wraplength=980)
        label.pack(fill=tk.BOTH, expand=True)

    def prompt_npc_data(self, npc=None):
        name = simpledialog.askstring("Input", "Name", initialvalue=npc.name if npc else "")
        if not name: return None
        race = simpledialog.askstring("Input", "Race", initialvalue=npc.race if npc else "")
        role = simpledialog.askstring("Input", "Role", initialvalue=npc.role if npc else "")
        stats = simpledialog.askstring("Input", "Stats (format: STR:DEX:CON:INT:WIS:CHA)", initialvalue=npc.stats if npc else "")
        armor_class = simpledialog.askstring("Input", "Armor Class", initialvalue=npc.armor_class if npc else "")
        attacks = simpledialog.askstring("Input", "Attacks", initialvalue=npc.attacks if npc else "")
        hit_points = simpledialog.askstring("Input", "Hit Points", initialvalue=npc.hit_points if npc else "")
        abilities = simpledialog.askstring("Input", "Abilities", initialvalue=npc.abilities if npc else "")
        equipment = simpledialog.askstring("Input", "Equipment", initialvalue=npc.equipment if npc else "")

        return {
            'name': name,
            'race': race,
            'role': role,
            'stats': stats,
            'armor_class': armor_class,
            'attacks': attacks,
            'hit_points': hit_points,
            'abilities': abilities,
            'equipment': equipment
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = NPCApp(root)
    root.mainloop()
