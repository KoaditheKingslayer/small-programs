import json

# Function to write data to a JSON file
def write_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print(f'Data has been written to {filename}')

# Function to read data from a JSON file
def read_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f'File {filename} not found.')
        return None

# Function to calculate total XP spent
def calculate_total_xp_spent(character_data):
    total_xp = 0

    # XP costs for different aspects (customize as needed)
    xp_costs = {
        "attributes": 5,
        "abilities": 2,
        "backgrounds": 1,
        "gifts": 3,
        # Add more elements and their XP costs as needed
    }

    # Calculate XP spent on attributes
    for value in character_data["attributes"].values():
        total_xp += xp_costs["attributes"] * value

    # Calculate XP spent on abilities
    for category, subcategories in character_data["abilities"].items():
        print(f"\n{category.capitalize()}:")
        
        if isinstance(subcategories, dict):
            for subcategory, values in subcategories.items():
                print(f"  {subcategory.capitalize()}:")
                
                if isinstance(values, dict):  # Check if values is a dictionary
                    for skill, rating in values.items():
                        print(f"    {skill.capitalize()}: {rating}")
                else:
                    print(f"    {subcategory.capitalize()}: {values}")
        else:
            if isinstance(subcategories, dict):  # Check if subcategories is a dictionary
                for skill, rating in subcategories.items():
                    print(f"  {skill.capitalize()}: {rating}")
            else:
                print(f"  {category.capitalize()}: {subcategories}")

    # Calculate XP spent on backgrounds
    for value in character_data["backgrounds"].values():
        total_xp += xp_costs["backgrounds"] * value

    # Calculate XP spent on gifts
    for gift in character_data["gifts"]:
        total_xp += xp_costs["gifts"] * gift["level"]

    # Add more calculations for other elements as needed

    return total_xp

# Sample data for a Werewolf character sheet
werewolf_character_sheet = {
    "player": "Your Name",
    "character_name": "Luna Howls",
    "breed": "Homid",
    "tribe": "Silver Fangs",
    "auspice": "Theurge",
    "rank": "Cliath",
    "attributes": {
        "strength": 4,
        "dexterity": 3,
        "stamina": 5,
        "charisma": 2,
        "manipulation": 3,
        "appearance": 4,
        "perception": 3,
        "intelligence": 2,
        "wits": 4
    },
    "abilities": {
        "talents": {
            "alertness": 3,
            "athletics": 2,
            "brawl": 4,
            "empathy": 2
        },
        "skills": {
            "crafts": 1,
            "drive": 2,
            "firearms": 1,
            "melee": 3
        },
        "knowledges": {
            "enigmas": 2,
            "occult": 3,
            "rituals": 4
        }
    },
    "backgrounds": {
        "ally": 2,
        "contacts": 3,
        "resources": 2,
        "totem": 4
    },
    "gifts": [
        {"name": "Heightened Senses", "level": 1},
        {"name": "Sense Wyrm", "level": 2},
        {"name": "Spirit Speech", "level": 1}
    ],
    "renown": {
        "glory": 3,
        "honor": 2,
        "wisdom": 1
    },
    "rage": 3,
    "gnosis": 5,
    "willpower": 6,
    "health": {
        "current": 7,
        "max": 7
    }
}

# Calculate total XP spent
werewolf_character_sheet["xp_spent"] = calculate_total_xp_spent(werewolf_character_sheet)

# Export data to a JSON file
json_filename = "werewolf_character_sheet.json"
write_to_json(werewolf_character_sheet, json_filename)

# Import data from the JSON file
imported_data = read_from_json(json_filename)

# Check if data was successfully imported
if imported_data:
    print("\nImported Werewolf Character Sheet:")
    print(f"Player: {imported_data['player']}")
    print(f"Character Name: {imported_data['character_name']}")
    print(f"Breed: {imported_data['breed']}")
    print(f"Tribe: {imported_data['tribe']}")
    print(f"Auspice: {imported_data['auspice']}")
    print(f"Rank: {imported_data['rank']}")
    print("\nAttributes:")
    for attribute, value in imported_data['attributes'].items():
        print(f"{attribute.capitalize()}: {value}")
    print("\nAbilities:")
    for category, subcategories in imported_data['abilities'].items():
        print(f"\n{category.capitalize()}:")
    if isinstance(subcategories, dict):
        for subcategory, values in subcategories.items():
            print(f"  {subcategory.capitalize()}:")
            if isinstance(values, dict):
                for skill, rating in values.items():
                    print(f"    {skill.capitalize()}: {rating}")
            else:
                print(f"    {subcategory.capitalize()}: {values}")
    else:
        print(f"  {category.capitalize()}: {subcategories}")

    print("\nBackgrounds:")
    for background, rating in imported_data['backgrounds'].items():
        print(f"{background.capitalize()}: {rating}")
    print("\nGifts:")
    for gift in imported_data['gifts']:
        print(f"{gift['name']} (Level {gift['level']})")
    print("\nRenown:")
    for renown, value in imported_data['renown'].items():
        print(f"{renown.capitalize()}: {value}")
    print(f"\nRage: {imported_data['rage']}")
    print(f"Gnosis: {imported_data['gnosis']}")
    print(f"Willpower: {imported_data['willpower']}")
    print("\nHealth:")
    print(f"Current: {imported_data['health']['current']}")
    print(f"Max: {imported_data['health']['max']}")
    print(f"\nTotal XP Spent: {imported_data['xp_spent']} XP")
