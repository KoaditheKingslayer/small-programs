import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.prompt import Prompt

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
        self.console = Console()
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

    def list_npcs(self):
        table = Table(title="NPC Catalog")

        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Race", style="magenta")
        table.add_column("Role", justify="right", style="green")

        for npc in self.npcs:
            table.add_row(npc.name, npc.race, npc.role)

        self.console.print(table)

    def view_npc(self, name):
        npc = next((npc for npc in self.npcs if npc.name == name), None)
        if npc:
            layout = Layout()
            layout.split_column(
                Layout(Panel(f"[bold]{npc.name}[/bold]\n[cyan]{npc.race}[/cyan]\n[green]{npc.role}[/green]")),
                Layout(Panel(f"[bold]Stats:[/bold] {npc.stats}")),
                Layout(Panel(f"[bold]Armor Class:[/bold] {npc.armor_class}")),
                Layout(Panel(f"[bold]Attacks:[/bold] {npc.attacks}")),
                Layout(Panel(f"[bold]Hit Points:[/bold] {npc.hit_points}")),
                Layout(Panel(f"[bold]Abilities:[/bold] {npc.abilities}")),
                Layout(Panel(f"[bold]Equipment:[/bold] {npc.equipment}")),
            )
            self.console.print(layout)
        else:
            self.console.print(f"[red]No NPC found with name {name}[/red]")

def main():
    catalog = NPCCatalog()

    while True:
        action = Prompt.ask("What would you like to do? (add/list/view/quit)", choices=["add", "list", "view", "quit"])
        
        if action == "add":
            name = Prompt.ask("Name")
            race = Prompt.ask("Race")
            role = Prompt.ask("Role")
            stats = Prompt.ask("Stats (format: STR:DEX:CON:INT:WIS:CHA)")
            armor_class = Prompt.ask("Armor Class")
            attacks = Prompt.ask("Attacks")
            hit_points = Prompt.ask("Hit Points")
            abilities = Prompt.ask("Abilities")
            equipment = Prompt.ask("Equipment")
            
            npc = NPC(name, race, role, stats, armor_class, attacks, hit_points, abilities, equipment)
            catalog.add_npc(npc)
        
        elif action == "list":
            catalog.list_npcs()
        
        elif action == "view":
            name = Prompt.ask("Enter the name of the NPC to view")
            catalog.view_npc(name)
        
        elif action == "quit":
            break

if __name__ == "__main__":
    main()
