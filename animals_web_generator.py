"""Print the data of every animal in animals_data.json."""
import json


def load_data(file_path):
    """Load and return the data of a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")
for animal in animals_data:
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])
    if animal.get("name"):
        print(f"Name: {animal['name']}")
    if characteristics.get("diet"):
        print(f"Diet: {characteristics['diet']}")
    if locations:
        print(f"Location: {locations[0]}")
    if characteristics.get("type"):
        print(f"Type: {characteristics['type']}")
    print()
