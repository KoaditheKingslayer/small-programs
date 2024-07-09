import json

# Function to load existing animals from file
def load_animals():
    try:
        with open("animals.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {"Animals": []}

# Function to add a new animal to the list
def add_animal(animal_list, new_animal):
    if "Animals" not in animal_list:
        animal_list["Animals"] = []
    animal_list["Animals"].append(new_animal)

# Function to prompt user for pet information
def get_pet_info():
    pet_name = input("Enter the pet's name: ")
    pet_type_category = input("Enter the pet's type category (e.g., Dog, Cat): ")
    pet_breed = input("Enter the pet's breed: ")
    pet_sex = input("Enter the pet's sex: ")
    pet_fur_color = input("Enter the pet's fur color: ")
    pet_age = input("Enter the pet's age: ")

    return {
        "Name": pet_name,
        "Type": {
            "Category": pet_type_category,
            "Breed": pet_breed
        },
        "Sex": pet_sex,
        "FurColor": pet_fur_color,
        "Age": pet_age
    }

# Function to view all animals in the JSON
def view_all_animals(animals_data):
    animals_list = animals_data.get("Animals", [])
    if not animals_list:
        print("No animals found.")
    else:
        print("\nAll Animals:")
        for animal in animals_list:
            print(json.dumps(animal, indent=2))
        print("\n")

# Main program
def main():
    while True:
        animals_data = load_animals()
        new_animal = get_pet_info()

        # Check for existing animals with the same name
        for existing_animal in animals_data.get("Animals", []):
            if existing_animal["Name"].lower() == new_animal["Name"].lower():
                print("Animal with the same name already exists. Adding as another animal.")
                break
        else:
            print("Adding a new animal.")
            add_animal(animals_data, new_animal)

        # Write the updated information to the JSON file
        with open("animals.json", "w") as json_file:
            json.dump(animals_data, json_file, indent=2)

        print("Animal information has been saved to 'animals.json'.")

        # Prompt user for next action
        user_choice = input("Enter 'e' to enter another animal, 'v' to view all animals, or any other key to exit: ")
        if user_choice.lower() == 'e':
            continue
        elif user_choice.lower() == 'v':
            view_all_animals(animals_data)
        else:
            break

if __name__ == "__main__":
    main()
